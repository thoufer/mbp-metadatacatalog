from django.test import TestCase, Client
from django.urls import reverse

#from asset.models import Asset
# from asset.views import (AssetCreateView,
#     AssetUpdateView,
#     AssetDetailView,
#     SubjectAutocomplete,
#     PlaceAutocomplete,
#     AssetTableView
#     )


class AssetTableViewTestCase(TestCase):
    """ Test asset listing table/view """
    def setUp(self):
        self.client = Client()

    def test_base_view(self):
            """ test using url resolver """
            response = self.client.get(reverse('asset:asset-table-listing'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('asset_list2.html')

    def test_one_entry(self):
        asset = asset.objects.create()


class AssetCreateViewTestCase(TestCase):
    """ Test view to create new asset objects """
    def setUp(self):
        pass

    def test_AssetCreateView(self):
        response = self.client.get(reverse('asset:add-asset'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/asset/add/')
        self.assertEqual(response.status_code, 200)


    def test_AssetUpdateView(self):
        pass

    def test_AssetDetailView(self):
        pass

    def test_SubjectAutocomplete(self):
        pass

    def test_PlaceAutocomplete(self):
        pass
