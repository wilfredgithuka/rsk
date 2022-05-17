from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.utils import timezone

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

# def HomeItemsView(request, id):
#     context = {}
#     context["data"] = HomeItems.objects.get(id = id)
#     return render(request,"home.html", context)


class HomeItemsView(DetailView):
    model = HomeItems
    #queryset = HomeItems.objects.all()
    template_name = 'home.html'
    context_object_name = 'data'

# class HomeItemsView(DetailView):
#     model = HomeItems
#     queryset = HomeItems.objects.all()
#     template_name = 'home.html'
#     context_object_name = 'homeitems'

# class HomeItemsView(DetailView):
#
#     model = HomeItems
#     template_name = 'home.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context
