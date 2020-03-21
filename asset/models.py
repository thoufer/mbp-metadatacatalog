from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase, ItemBase
from simple_history.models import HistoricalRecords

from .validators import validate_primary_email, validate_start_year, validate_end_year, validate_name


class Organization(models.Model):
    """
    Model store organization information.  Org Codes are derived from the FWS
    Corporate Master Table (CMT).
    http://intranet.fws.gov/cmt/
    """
    code = models.PositiveIntegerField(primary_key=True)
    region = models.CharField(max_length=2, blank=False)
    name = models.CharField(max_length=150, blank=False)

    def save(self, *args, **kwargs):
        """
        Every org is part of a FWS admin region. Make it a property, which
        is the first digit of the org code. R9 == Headquarters.
        """
        region = str(self.code)[0]
        if region == '9':
            self.region = 'HQ'
        else:
            self.region = 'R{}'.format(region)

        super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return self.region + ' - ' + self.name

    class Meta:
        ordering = ['code']
        db_table = 'organization'
        verbose_name = 'Organization'


class SubjectTag(TagBase):
    """ Base table to store subject tags. """
    class Meta:
        ordering = ['name']
        verbose_name = _("Subject Tag")
        verbose_name_plural = _("Subject Tags")


class LocationTag(TagBase):
    """ Base table to store location tags. """
    class Meta:
        ordering = ['name']
        verbose_name = _("Location Tag")
        verbose_name_plural = _("Location Tags")


class TaggedSubject(TaggedItemBase):
    """
    Link or join table between Asset and Tags
    """
    content_object = models.ForeignKey("Asset",
        on_delete=models.CASCADE,
        )
    tag = models.ForeignKey("SubjectTag",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
        )

    class Meta:
        db_table = 'AssetSubject_Tag'


class TaggedPlace(TaggedItemBase):
    """
    Link or join table between Asset and Tags
    """
    content_object = models.ForeignKey("Asset",
        on_delete=models.CASCADE,
        )
    tag = models.ForeignKey("LocationTag",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
        )

    class Meta:
        db_table = 'AssetPlace_Tag'


class Asset(models.Model):
    """
    Store metadata information associated with data asset.
    """
    status_choices =(
        ('', 'Choose status'),
        ('Operational','Operational'),
        ('Inactive','Inactive'),
        ('Experimental','Experimental'),
        )

    spatial_scale_choices = (
        ('', 'Choose Scale'),
        ('BCR','BCR'),
        ('Multiple states or provinces','Multiple states or provinces'),
        ('Single state or province','Single state or province'),
        ('Local','Local'),
        )

    month_choices = (
        ('', 'Choose'),
        ('JAN', 'January'),
        ('FEB', 'February'),
        ('MAR', 'March'),
        ('APR', 'April'),
        ('MAY', 'May'),
        ('JUN', 'June'),
        ('JUL', 'July'),
        ('AUG', 'August'),
        ('SEP', 'September'),
        ('OCT', 'October'),
        ('NOV', 'November'),
        ('DEC', 'December'),
        )

    state_choices = (
        ('', 'State'),
        ('AL','AL'),('AK','AK'),('AZ','AZ'),('AR','AR'),('CA','CA'),('CO','CO'),
        ('CT','CT'),('DE','DE'),('DC','DC'),('FL','FL'),('GA','GA'),('HI','HI'),
        ('ID','ID'),('IL','IL'),('IN','IN'),('IA','IA'),('KS','KS'),('KY','KY'),
        ('LA','LA'),('ME','ME'),('MD','MD'),('MA','MA'),('MI','MI'),('MN','MN'),
        ('MS','MS'),('MO','MO'),('MT','MT'),('NE','NE'),('NV','NV'),('NH','NH'),
        ('NJ','NJ'),('NM','NM'),('NY','NY'),('NC','NC'),('ND','ND'),('OH','OH'),
        ('OK','OK'),('OR','OR'),('PA','PA'),('PR','PR'),('RI','RI'),('SC','SC'),
        ('SD','SD'),('TN','TN'),('TX','TX'),('UT','UT'),('VT','VT'),('VA','VA'),
        ('VI','VI'),('WA','WA'),('WV','WV'),('WI','WI'),('WY','WY'),
        )

    organization = models.ForeignKey('Organization',
        related_name='assets',
        on_delete=models.PROTECT,
        verbose_name=_('Primary Organization of Stewardship'),
        )
    parent = models.ForeignKey('self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Parent Asset'),
        related_name='child_asset',
        help_text=_("If this data asset shares a common history, administration, "
                    "decision context, and/or species + location + platform that "
                    "requires coordinated planning and management, select the "
                    "assest that is its parent.")
        )
    name = models.CharField(_('Name'),
        max_length=200,
        blank=False,
        help_text=_('A descriptive name of the asset.')
        )
    status = models.CharField(_('Status'),
        max_length=23,
        blank=False,
        choices=status_choices,
        help_text=_("Select the value that best represents the current status "
            "of the asset. `Inactive` should be used for assets that have ceased "
            "operations or have been discontinued.")
        )
    isContracted = models.BooleanField(_('Contracted'),
        default=False,
        help_text=_("Check this for assets in which the storage or maintenance of"
                    "the asset are performed through a contractual "
                    "aggreeement with a non-fws entity.")
        )
    spatial_scale = models.CharField(
        max_length=50,
        blank=False,
        choices= spatial_scale_choices,
        help_text=_("Choose the spatial scale that best represents the largest "
                    "scale that the data are collected.")
        )
    start_month = models.CharField(_('Collection start month'),
        max_length=3,
        blank=True,
        null=True,
        choices=month_choices)
    end_month = models.CharField(_('Collection end month'),
        max_length=3,
        blank=True,
        null=True,
        choices=month_choices)
    subject_tags = TaggableManager(through=TaggedSubject,
        related_name='subject_tags',
        verbose_name=_('Keywords'),
        help_text=_('Select all that apply. Additional keywords can be created by typing '
                    'the desired keyword, followed by selecting it from the menu or &lt;Enter&gt;.')
        )
    place_tags = TaggableManager(through=TaggedPlace,
        related_name='place_tags',
        verbose_name=_('Location keywords'),
        help_text=_('Select all that apply. Additional keywords can be created by typing '
                    'the desired keyword, followed by selecting it from the menu or &lt;Enter&gt;.')
        )
    description = models.TextField(_('Abstract'),
        max_length=10000,
        help_text=_("Enter a description which provides detailed "
                    "information about the use, timing, location, and methods "
                    "of data collection or analysis. (Max 10,000 characters)")
        )
    partners = models.CharField(_('Partners'),
        max_length = 5000,
        blank=True,
        null=True,
        help_text=_("Include all partners as a comma separated list, that have direct "
                    "involvement in the collection, storage, or maintenance of the asset.")
        )
    start_year = models.CharField(_('Starting Year'),
        max_length=4,
        blank=True,
        null=True,
        validators=[validate_start_year],
        help_text=_('The year in which data were first collected')
        )
    end_year = models.CharField(_('Ending Year'),
        max_length=7,
        blank=True,
        null=True,
        validators=[validate_end_year],
        help_text=_("The last year data were collected, or `Present` if the "
                    "data are still being collected.")
        )
    primary_contact_name = models.CharField(_('Primary Contact'),
        max_length=50,
        blank=False,
        validators=[validate_name]
        )
    primary_contact_address1= models.CharField(_('Address'), max_length=150, blank=False)
    primary_contact_address2= models.CharField(_('Address 2'), max_length=150, blank=True, null=True)
    primary_contact_city = models.CharField(_('City'), max_length=50, blank=False)
    primary_contact_state = models.CharField(_('State'),
        max_length=2,
        blank=False,
        choices=state_choices
        )
    primary_contact_zip = models.CharField(_('Zip'), max_length=5, blank=False)
    primary_contact_email = models.EmailField(_('Email'), blank=False, validators=[validate_primary_email])
    primary_contact_phone = models.CharField(_('Phone'), max_length=14, blank=False)
    primary_contact_phone_ext = models.CharField(_('Extension'), max_length=4, blank=True, null=True)
    data_contact_name = models.CharField(_('Data Contact'), max_length=50, blank=False, validators=[validate_name])
    data_contact_address1 = models.CharField(_('Address'), max_length=150, blank=False)
    data_contact_address2 = models.CharField(_('Address 2'), max_length=150, blank=True, null=True)
    data_contact_city = models.CharField(_('City'), max_length=50, blank=False)
    data_contact_state = models.CharField(_('State'),
        max_length=2,
        blank=False,
        choices=state_choices
        )
    data_contact_zip = models.CharField(_('Zip'), max_length=5, blank=False)
    data_contact_email = models.EmailField(_('Email'), blank=False)
    data_contact_phone = models.CharField(_('Phone'), max_length=14, blank=False)
    data_contact_phone_ext = models.CharField(_('Extension'), max_length=4, blank=True, null=True)
    history = HistoricalRecords(table_name='asset_history')
    created = models.DateTimeField(_('Created'), auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(_('Last Update'), auto_now=True, blank=True, null=True)

    @property
    def subject_taglist(self):
        """ return comma separated list of subject tags for object """
        # TODO it seems like self.subject_tags.names() might be more useful
        tags = self.subject_tags.all().distinct()
        return ', '.join(t.name for t in tags)

    @property
    def place_taglist(self):
        """ return comma separated list of place tags for object """
        tags = self.place_tags.all().distinct()
        return ', '.join(t.name for t in tags)

    def __str__(self):
        return "({}) - {}".format(str(self.id), self.name)

    class Meta:
        db_table = 'Asset'
        ordering = ['id',]
