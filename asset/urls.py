from django.urls import path

from .views import (
    AssetCreateView,
    AssetDetailView,
    AssetUpdateView,
    SubjectAutocomplete,
    PlaceAutocomplete,
    AssetAPI,
    )

app_name = 'asset'

urlpatterns = [
    path('detail/<int:pk>/', AssetDetailView.as_view(), name='detail-asset'),
    path('add/', AssetCreateView.as_view(), name='add-asset'),
    path('edit/<int:pk>/', AssetUpdateView.as_view(), name='update-asset'),
    path('api/subject-autocomplete', SubjectAutocomplete.as_view(), name='get-subject-tags'),
    path('api/place-autocomplete', PlaceAutocomplete.as_view(), name='get-place-tags'),
    path('api/asset', AssetAPI.as_view({'get':'list'}), name='api-asset'),
]
