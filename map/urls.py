from . import views
from django.urls import path

urlpatterns = [
    path('map', views.BeaconView.as_view(), name='beacon_map'),
]
