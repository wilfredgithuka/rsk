from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('', views.HomeItemsView.as_view(),name='home2'),
]
