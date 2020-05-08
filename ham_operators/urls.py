from . import views
from django.urls import path

urlpatterns = [
    path('', views.OperatorList.as_view(), name='operators'),
]
