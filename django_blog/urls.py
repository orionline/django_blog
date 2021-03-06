"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from article.views import PostRssFeed
from django.contrib.syndication.views import Feed

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^static/','django.views.static.serve',{'document_root':settings.STATIC_ROOT},name='static'),
    url(r'^$', 'article.views.home', name='home'),
    url(r'^create_blog/$', 'article.views.create_blog', name = 'create_blog'),
    url(r'^search/','article.views.blog_search', name = 'search'),
    url(r'^about/$', 'article.views.about', name='about'),
    url(r'^feed/$', PostRssFeed(), name = "RSS"),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^(?P<category>[\w\-]+)/$', 'article.views.search_category', name = 'search_category'),
    url(r'^modify/(?P<id>\d+)/$', 'article.views.modify', name="modify"),
    url(r'^delete/(?P<id>\d+)/$', 'article.views.delete', name="delete"),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)