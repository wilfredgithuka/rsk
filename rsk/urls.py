"""rsk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.flatpages import views
from django.conf import settings
from django.conf.urls.static import static


X_FRAME_OPTIONS = 'SAMEORIGIN'

urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    #path('', include('map.urls')),
    path('blog/', include ('blog.urls')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('callbook/', include('ham_operators.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('manuals/', include('manuals.urls')),
    #path('files_list/',include('downloads.urls')),
    #path(r'^download/(?P<file_name>.+)$', 'downloads.views.download'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns = patterns('',
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    #) + urlpatterns



    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), + urlpatterns
