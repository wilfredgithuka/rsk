from . import views
from django.urls import path
from .views import HomeItemsView

urlpatterns = [
    path('<pk:pk/', views.HomeItemsView.as_view(), name='home'),
    path('', views.HomePageView.as_view(), name='home'),

]
