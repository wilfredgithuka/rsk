from django import shortcuts
from django.views import generic

import models


class ArticleListView(generic.ListView):

    paginate_by = 8
    kind = None

    def get_queryset(self):
        if self.kind:
            return models.Article.objects.published().filter(kind=self.kind)
        else:
            return models.Article.objects.published()

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)

        context['kind'] = self.kind

        return context


class ArticleDetailView(generic.DetailView):

    model = models.Article

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.get_absolute_url() != self.request.path:
            return shortcuts.redirect(self.object, permanent=True)

        # See: super(ArticleDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

        # TODO: Find a way to call super() without retrieving the object twice
        # super(ArticleDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        obj = shortcuts.get_object_or_404(queryset, pk=self.kwargs.get('id'),
                                          status='p')

        return obj
