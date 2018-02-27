from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django_tables2 import RequestConfig, SingleTableMixin
from django_filters.views import FilterView
from dal import autocomplete

from .models import Asset, TaggedSubject, TaggedPlace, SubjectTag, LocationTag
from .tables import AssetListTable
from .forms import AssetCreateForm, AssetListFormHelper, AssetFilterForm
from .filters import AssetFilter
from .utils import PagedFilteredTableView


class AssetCreateView(SuccessMessageMixin, CreateView):
    """ """
    model = Asset
    template_name = 'asset_create.html'
    form_class = AssetCreateForm
    success_url = reverse_lazy('asset:asset-table-listing')
    success_message = "%(name)s was created successfully"


class AssetUpdateView(UpdateView):
    """ """
    model = Asset
    template_name = 'asset_create.html'
    form_class = AssetCreateForm
    #success_message = ""
    success_url = reverse_lazy('asset:asset-table-listing')


class AssetDetailView(DetailView):
    """
    Display non-editable details for asset object.
    """
    model = Asset
    context_object_name = 'asset'
    template_name = 'asset_detail.html'


class SubjectAutocomplete(autocomplete.Select2QuerySetView):
    """
    API view to return subject tags for autocomplete.
    """
    def has_add_permission(self, request):
        """
        Override the default to require a user to be authenticated in order to add tags.
        This may turn out to be a bad idea if abused by users.
        """
        return True

    def get_queryset(self):
        qs = SubjectTag.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class PlaceAutocomplete(autocomplete.Select2QuerySetView):
    """
    API view to retun place tags for autocomplete
    """
    def has_add_permission(self, request):
        """
        Override the default to require a user to be authenticated in order to add tags.
        This may turn out to be a bad idea if abused by users.
        """
        return True

    def get_queryset(self):
        qs = LocationTag.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class AssetTableView(PagedFilteredTableView):
    """ """
    model = Asset
    template_name = 'asset_list2.html'
    table_class = AssetListTable
    paginate_by = 25
    filter_class = AssetFilter
    formhelper_class = AssetListFormHelper
