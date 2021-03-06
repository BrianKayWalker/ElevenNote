"""elevennote URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from tastypie.api import Api
from note.api.resources import UserResource, NoteResource
from note.auth_views import RegisterView

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(NoteResource())

urlpatterns = [
    # Handle the root url.
    url(r'^$', lambda r: HttpResponseRedirect('notes/')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Registration
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {"next_page" : reverse_lazy('login')}, name='logout'),

    url('^register/', RegisterView.as_view(), name='register'),

    # Our app
    url(r'^notes/', include('note.urls', namespace="note")),
    
    # Our API
    url(r'^api/', include(v1_api.urls)),

]
