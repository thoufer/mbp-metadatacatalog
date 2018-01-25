import django_filters
from django import forms

from .models import Asset

class AssetFilter(django_filters.FilterSet):
    """
    """
    name = django_filters.CharFilter(lookup_expr="icontains",
            widget= forms.TextInput(attrs={'placeholder': 'Name contains'}))
    organization__region = django_filters.CharFilter(lookup_expr="icontains",
            widget= forms.TextInput(attrs={'placeholder': 'Region (R#|HQ)'}))

    class Meta:
        model = Asset
        fields = ['organization__region','status',]
