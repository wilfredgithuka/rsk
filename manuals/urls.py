from django.urls import path
from .views import ManualsList
from . import views

urlpatterns = [
    path('', views.ManualsList.as_view()),
]
