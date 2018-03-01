import django_tables2 as tables
from django_tables2 import A, SingleTableView

from .models import Asset

class AssetListTable(tables.Table):
    """
    Create table of assets in Database.
    """
    region = tables.Column(accessor='organization.region')
    OrgName = tables.Column(verbose_name='Stewardship Organization', accessor='organization.name')
    details = tables.LinkColumn('asset:detail-asset',
                                verbose_name="",
                                text= "Details",
                                args=[A('pk')],
                                orderable=False,
                                )

    class Meta:
        model = Asset
        fields = ['name','status','spatial_scale']
        attrs = {'class': "table table-hover table-striped"}
        empty_text = "No Assets found"
        sequence = ('name','status','OrgName','region','spatial_scale',)
