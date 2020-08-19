from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import HomeItems
from django.views import generic
from map.utils import generate_beacon_map

class HomePageView(TemplateView):
    template_name="home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        beacon_map = generate_beacon_map()
        context["beacon_map"] = beacon_map
        return context

class HomeItemsView(DetailView):
    model = HomeItems
