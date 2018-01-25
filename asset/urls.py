from django.urls import path

from .views import (AssetListView,
    AssetCreateView,
    AssetListView,
    AssetDetailView,
    AssetUpdateView,
    SubjectAutocomplete,
    PlaceAutocomplete,
    AssetTableView, AssetTableView2,
    )

app_name = 'asset'

urlpatterns = [
    #path('', AssetListView.as_view(), name='list-asset'),
    path('', AssetTableView.as_view(), name='asset-table-listing'),
    #path('FilterTable/', AssetTableView2.as_view(), name='asset-table2'),
    path('detail/<int:pk>/', AssetDetailView.as_view(), name='detail-asset'),
    path('add/', AssetCreateView.as_view(), name='add-asset'),
    path('edit/<int:pk>/', AssetUpdateView.as_view(), name='update-asset'),
    path('api/subject-autocomplete', SubjectAutocomplete.as_view(create_field='name'), name='get-subject-tags'),
    path('api/place-autocomplete', PlaceAutocomplete.as_view(create_field='name'), name='get-place-tags'),
]
