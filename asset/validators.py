from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import re
import datetime

def validate_start_year(value):
    """
    Since our datasets are modern they must have start years in 19XX or 20XX.
    Raise error if year is not between that range or year is in the future.
    """
    if re.match("^19[0-9]{2}|^20[01]{1}[0-9]{1}$", value) is None:
        raise ValidationError(
            _('{value} falls outside reasonale year bounds').format(value=value)
        )

    if int(value) > datetime.date.today().year:
        raise ValidationError(
            _('Start year cannot be in the future.')
        )


def validate_end_year(value):
    """
    If survey is ongoing, then the acceptable value is Present.
    """
    if re.match('^19[0-9]{2}|^20[01]{1}[0-9]{1}$|^Present$', value) is None:
        raise ValidationError(
            _('{value} is not a valid ending year.').format(value=value)
        )

        if int(value) > datetime.date.today().year:
            raise ValidationError(
                _('{value} is in the future, use Present for ongoing data collection.').format(value=value)
            )


def validate_primary_email(value):
    """
    The primary contact person must be a Fish and Wildlife Service employee.
    Verify this by requiring that the email for this person is in the fws.gov
    domain.
    """
    if not 'fws.gov' in value:
        raise ValidationError(
            _('The primary contact person must be a FWS employee.')
        )

def validate_name(value):
    """
    A persons name can only contain Aa-Zz and an apostrophe for the Irish or hyphens for hyphenated surnames.
    """
    if re.match("^[\W*|\w[-]\w*$|\d'{1}\d]", value) is not None:
        raise ValidationError(
            _('Name may contain only alphabetic characters, apostrophes, & hyphens.')
        )
