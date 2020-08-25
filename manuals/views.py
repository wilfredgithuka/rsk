from django.shortcuts import render
from .models import Manuals
from django.views.generic.list import ListView
from django.views import generic

#class ManualsView(ListView):
#    model = Manuals
#    template_name = 'downloads.html'


#class ManualsView(ListView):
#    model = Manuals
#    template_name = 'downloads.html'
#    queryset = Manuals.objects.all()
#    context_object_name = 'Manuals'
#    paginate_by = 10

class ManualsList(generic.ListView):
    queryset = Manuals.objects.order_by('-created_on')
    template_name = 'downloads.html'
    paginate_by = 30
