from rest_framework import serializers

from .models import Asset, Organization, TaggedSubject, SubjectTag

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('region','name',)


class AssetSerializer(serializers.ModelSerializer):
    """ Asset model serializer """
    organization = OrganizationSerializer()

    class Meta:
        model = Asset
        fields = ('id','name','status','organization','spatial_scale','child_asset','subject_taglist','place_taglist',)

    def get_fields(self):
        fields = super(AssetSerializer, self).get_fields()
        fields['child_asset'] = AssetSerializer(many=True)
        return fields
