from . import views
from django.urls import path

urlpatterns = [
    path('', views.BeaconView.as_view(), name='map'),
]
