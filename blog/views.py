from django.shortcuts import render
from .models import Post
from django.views import generic
from django.views.generic import TemplateView
from map.utils import generate_beacon_map

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        beacon_map = generate_beacon_map()
        context ["beacon_map"] = beacon_map
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
