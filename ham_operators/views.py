from django.shortcuts import render
from django.views import generic

from .models import Operator

class OperatorList(generic.ListView):
    queryset = Operator.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# Create your views here.
