from django.conf import urls

import views
import models


urlpatterns = urls.patterns(
    '',
    urls.url(r'^articles/(?P<id>[\d]+)(?:/(?P<slug>[\S]+))?/$',
             views.ArticleDetailView.as_view(), name='article_detail'),
    urls.url(r'^articles/$', views.ArticleListView.as_view(kind=models.Article.KIND_ARTICLE),
             name='article_list'),
    urls.url(r'^blog/$', views.ArticleListView.as_view(kind=models.Article.KIND_BLOG),
             name='blog_list'),
)
