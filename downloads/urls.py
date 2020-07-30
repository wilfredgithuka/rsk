from . import views
from django.urls import path



urlpatterns = [
    path('', views.DjangoFileView.as_view()),
    ]
