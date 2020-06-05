from django.shortcuts import render
from django.views.generic import TemplateView
import folium
from folium import plugins
import ipywidgets
import geocoder
import geopy
import numpy as np
import pandas as pd
import os
import urllib.request
import matplotlib.pyplot as plt


class BeaconView(TemplateView):
    template_name = "index.html"

    def map_data(self, **kwargs):
        kenya = folium.Map(location=[-1.28333, 36.81667], zoom_start=12, width=400, height=300, control_scale=True)

        folium.Marker(location= [-1.303640, 36.785963], zoom_start=12, popup='RSK Radio Shack 5Z4RS', tooltip='5Z4RS Radio Shack').add_to(kenya)
        folium.Marker(location=[-1.296058, 36.761117], zoom_start=12, popup = 'NCDXF beacon 5Z4B & 2m Repeater', tooltip='NCDXF Beacon 5Z4B').add_to(kenya)
        folium.Marker(location=[-1.262335, 36.757378], zoom_start=12, popup = 'Communications Authority of Kenya', tooltip='CA Kenya').add_to(kenya)
        folium.Marker(location=[-1.245479, 36.771003], zoom_start=12, popup = 'Planning House, Lower Kabete', tooltip='Planning Hse').add_to(kenya)

        kenya.save('rsk.html')
        kenya.render()

        context = {'map': kenya._repr_html_()}
        return render(request, 'index.html', context)


# {'my_map': map} will output the object, which is what you are seeing
# to rectify this we need to turn it into an iframe which 
# the template can then render.
