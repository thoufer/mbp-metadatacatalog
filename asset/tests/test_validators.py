from django.test import TestCase
from django.core.exceptions import ValidationError

from asset.validators import validate_start_year, validate_end_year, validate_primary_email, validate_name

class ValidatorsTestCase(TestCase):

    def test_valiidate_start_year(self):
        """ """
        with self.assertRaises(ValidationError):
            validate_start_year('1900')
            validate_start_year('2019')

    def test_validate_end_year(self):
        """ """
        with self.assertRaises(ValidationError):
            validate_end_year('1900')
            validate_end_year('2019')
            validate_end_year('Preseant')

    def test_validate_name(self):
        """ """
        with self.assertRaises(ValidationError):
            validate_name('Nathan_zimpfer')
            validate_name('Nathan zimpfer@fws.gov')
            validate_name('bob Smit?')
            validate_name("Nancy O'Dell")  # This is valid and test should fail..
