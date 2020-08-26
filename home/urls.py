from . import views
from django.urls import path
#from .views import HomeItemsView

urlpatterns = [
    #path('test/<int:pk>/', views.HomeItemsView.as_view()),
    path('', views.HomePageView.as_view(), name='home'),

]
