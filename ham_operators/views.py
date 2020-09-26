from django.shortcuts import render
from django.views import generic

from .models import Operator

class OperatorList(generic.ListView):
    queryset = Operator.objects.order_by('-created_on')
    template_name = 'callbook.html'
