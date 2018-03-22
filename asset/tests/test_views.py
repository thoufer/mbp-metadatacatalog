from django.test import TestCase, Client
from django.urls import reverse

from asset.models import Organization, Asset
from asset.views import (AssetCreateView,
     AssetUpdateView,
     AssetDetailView,
     )


class AssetCreateViewTestCase(TestCase):
    """ Test view to create new asset objects """

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/asset/add/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessbile_by_name(self):
        response = self.client.get(reverse('asset:add-asset'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('asset:add-asset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset_create.html')


class AssetUpdateViewTestCase(TestCase):
    """ Test view for updating assets """

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

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/asset/edit/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessbile_by_name(self):
        response = self.client.get(reverse('asset:update-asset', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('asset:update-asset', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset_create.html')


class AssetDetailViewTestCase(TestCase):
    """ Test view which displays asset details. """

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

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/asset/detail/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessbile_by_name(self):
        response = self.client.get(reverse('asset:detail-asset', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('asset:detail-asset', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset_detail.html')
