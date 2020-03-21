from django.db.models.query import Prefetch
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core.mail import mail_admins
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.template.loader import render_to_string
from rest_framework import generics, viewsets
from django_tables2 import RequestConfig, SingleTableMixin
from django_filters.views import FilterView
from dal import autocomplete

from .models import Asset, TaggedSubject, TaggedPlace, SubjectTag, LocationTag
from .forms import AssetCreateForm
from .filters import AssetFilter
from .serializers import AssetSerializer


class AssetCreateView(SuccessMessageMixin, CreateView):
    """ """
    model = Asset
    template_name = 'asset_create.html'
    form_class = AssetCreateForm
    success_url = reverse_lazy('asset-table-listing')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        """ Send an email to admins notifying them that a new asset has been created, for review. """
        msg = render_to_string('asset_create_email.txt',
            {
            'name': form.cleaned_data.get('name'),
            'organization': form.cleaned_data.get('organization'),
            'description': form.cleaned_data.get('description'),
            'primary_contact_name': form.cleaned_data.get('primary_contact_name'),
            'primary_contact_email': form.cleaned_data.get('primary_contact_email')
            })
        mail_admins(subject="New asset added", message=msg)

        return super(AssetCreateView, self).form_valid(form)


class AssetUpdateView(UpdateView):
    """ """
    model = Asset
    template_name = 'asset_create.html'
    form_class = AssetCreateForm
    #success_message = ""
    success_url = reverse_lazy('asset-table-listing')


class AssetDetailView(DetailView):
    """
    Display non-editable details for asset object.
    """
    model = Asset
    context_object_name = 'asset'
    template_name = 'asset_detail.html'

    def get_object(self):
        return Asset.objects.prefetch_related(Prefetch('child_asset', to_attr="sub_assets")).get(pk=self.kwargs['pk'])


# Views for API calls below
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


class AssetAPI(viewsets.ReadOnlyModelViewSet):
    """
    A basic viewset for viewing assets.
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
