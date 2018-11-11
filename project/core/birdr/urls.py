from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path
from django.views.generic import TemplateView


import birds.urls
import nets.urls
import profiles.urls
import stations.urls

urlpatterns = [

    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^', include(('birds.urls', 'birds'), namespace='birds')),
    url(r'^', include(('nets.urls', 'nets'), namespace='nets')),
    url(r'^', include(('profiles.urls', 'profiles'), namespace='profiles')),
    url(r'^', include(('stations.urls', 'stations'), namespace='stations')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
]