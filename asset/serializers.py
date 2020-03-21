from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                          TaggitSerializer)

from .models import Asset, Organization

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('region','name',)


class AssetSerializer(TaggitSerializer, serializers.ModelSerializer):
    """ Asset model serializer """
    organization = OrganizationSerializer()
    subject_tags = TagListSerializerField()
    place_tags =  TagListSerializerField()

    class Meta:
        ordering = ['name',]
        model = Asset
        fields = ('id', 'name', 'organization', 'status', 'description', 'isContracted', 'spatial_scale',
                    'start_month', 'end_month', 'start_year', 'end_year', 'partners', 'primary_contact_name',
                    'primary_contact_address1', 'primary_contact_address2', 'primary_contact_city',
                    'primary_contact_state', 'primary_contact_zip', 'primary_contact_phone', 'primary_contact_email',
                    'data_contact_name', 'data_contact_address1', 'data_contact_address2', 'data_contact_city',
                    'data_contact_state','data_contact_zip', 'data_contact_phone', 'data_contact_email',
                    'subject_tags', 'place_tags', 'created', 'last_modified',)

    def get_fields(self):
        fields = super(AssetSerializer, self).get_fields()
        return fields
