from django.test import TestCase

from asset.models import (Organization, Asset, SubjectTag, LocationTag,
    TaggedSubject, TaggedPlace, )

class OrganizationTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(code=10111, name='Migratory Bird Program')
        Organization.objects.create(code=90120, name='Branch of Monitoring and Data Management')

    def test_code_label(self):
        organization= Organization.objects.get(code=10111)
        field_label = organization._meta.get_field('code').verbose_name
        self.assertEquals(field_label,'code')

    def test_region_label(self):
        organization= Organization.objects.get(code=10111)
        field_label = organization._meta.get_field('region').verbose_name
        self.assertEquals(field_label,'region')

    def test_name_label(self):
        organization= Organization.objects.get(code=10111)
        field_label = organization._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_region_max_length(self):
        organization= Organization.objects.get(code=10111)
        max_length = organization._meta.get_field('region').max_length
        self.assertEquals(max_length, 2)

    def test_name_max_length(self):
        organization= Organization.objects.get(code=10111)
        max_length = organization._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)

    def test_object_name_is_region_hypen_name(self):
        organization= Organization.objects.get(code=10111)
        expected_object_name = '%s - %s' % (organization.region, organization.name)
        self.assertEquals(expected_object_name, str(organization))

    def test_region_value(self):
        regional_org = Organization.objects.get(code=10111)
        self.assertEquals('R1', regional_org.region)

        headquarters_org = Organization.objects.get(code=90120)
        self.assertEquals('HQ', headquarters_org.region)


class AssetTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        organization = Organization(code=90210, name='Division Of Migratory Bird Management')

        asset = Asset.objects.create(organization=organization,
            name='Waterfowl Breeding Population and Habitat Survey',
            status='Operational',
            spatial_scale='Local',
            start_month='May',
            end_month='July',
            description='Some Text for an Abstract',
            partners='CWS, USGS',
            start_year='1955',
            end_year='Present',
            primary_contact_name='John Smith',
            primary_contact_address1='1600 Pennslyvania Ave.',
            primary_contact_city='Washington',
            primary_contact_state='DC',
            primary_contact_zip='20320',
            primary_contact_phone='(123) 876-5309',
            primary_contact_email='John_smith@fws.gov',
            data_contact_name='John Smith',
            data_contact_address1='1600 Pennslyvania Ave.',
            data_contact_city='Washington',
            data_contact_state='DC',
            data_contact_zip='20320',
            data_contact_phone='(123) 876-5309',
            data_contact_email='John_smith@fws.gov')
        asset.subject_tags.add('Aerial Survey', 'Ground Survey', 'Waterfowl', 'Loons')
        asset.place_tags.add('US', 'Canada')

    def test_organization_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('organization').verbose_name
        self.assertEquals(field_label,'Primary Organization of Stewardship')

    def test_parent_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('parent').verbose_name
        self.assertEquals(field_label,'Parent Asset')

    def test_name_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Name')

    def test_status_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('status').verbose_name
        self.assertEquals(field_label,'Status')

    def test_isContracted_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('isContracted').verbose_name
        self.assertEquals(field_label,'Contracted')

    def test_spatial_scale_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('spatial_scale').verbose_name
        self.assertEquals(field_label,'spatial scale')

    def test_start_month_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('start_month').verbose_name
        self.assertEquals(field_label,'Collection start month')

    def test_end_month_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('end_month').verbose_name
        self.assertEquals(field_label,'Collection end month')

    def test_subject_tags_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('subject_tags').verbose_name
        self.assertEquals(field_label,'Description keywords')

    def test_place_tags_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('place_tags').verbose_name
        self.assertEquals(field_label,'Location keywords')

    def test_description_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'Abstract')

    def test_partners_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('partners').verbose_name
        self.assertEquals(field_label,'Partners')

    def test_start_year_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('start_year').verbose_name
        self.assertEquals(field_label,'Starting Year')

    def test_end_year_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('end_year').verbose_name
        self.assertEquals(field_label,'Ending Year')

    def test_primary_contact_name_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_name').verbose_name
        self.assertEquals(field_label,'Primary Contact')

    def test_primary_contact_address1_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_address1').verbose_name
        self.assertEquals(field_label,'Address')

    def test_primary_contact_address2_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_address2').verbose_name
        self.assertEquals(field_label,'Address 2')

    def test_primary_contact_city_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_city').verbose_name
        self.assertEquals(field_label,'City')

    def test_primary_contact_state_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_state').verbose_name
        self.assertEquals(field_label,'State')

    def test_primary_contact_zip_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_zip').verbose_name
        self.assertEquals(field_label,'Zip')

    def test_primary_contact_phone_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_phone').verbose_name
        self.assertEquals(field_label,'Phone')

    def test_primary_contact_phone_ext_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_phone_ext').verbose_name
        self.assertEquals(field_label,'Extension')

    def test_primary_contact_email_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('primary_contact_email').verbose_name
        self.assertEquals(field_label,'Email')

    def test_data_contact_name_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_name').verbose_name
        self.assertEquals(field_label,'Data Contact')

    def test_data_contact_address1_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_address1').verbose_name
        self.assertEquals(field_label,'Address')

    def test_data_contact_address2_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_address2').verbose_name
        self.assertEquals(field_label,'Address 2')

    def test_data_contact_city_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_city').verbose_name
        self.assertEquals(field_label,'City')

    def test_data_contact_state_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_state').verbose_name
        self.assertEquals(field_label,'State')

    def test_data_contact_zip_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_zip').verbose_name
        self.assertEquals(field_label,'Zip')

    def test_data_contact_phone_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_phone').verbose_name
        self.assertEquals(field_label,'Phone')

    def test_data_contact_phone_ext_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_phone_ext').verbose_name
        self.assertEquals(field_label,'Extension')

    def test_data_contact_email_label(self):
        asset = Asset.objects.get(id=1)
        field_label = asset._meta.get_field('data_contact_email').verbose_name
        self.assertEquals(field_label,'Email')

    def test_object_name(self):
        asset = Asset.objects.get(id=1)
        expected_object_name = '(%s) - %s' % (asset.id, asset.name)
        self.assertEquals(expected_object_name, str(asset))

    def test_subject_taglist_property(self):
        asset = Asset.objects.get(id=1)
        self.assertEqual(asset.subject_taglist, "Aerial Survey, Ground Survey, Loons, Waterfowl")

    def test_place_taglist_property(self):
        asset = Asset.objects.get(id=1)
        self.assertEqual(asset.place_taglist, "Canada, US")
