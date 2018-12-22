from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path

import birds.urls
import profiles.urls
import stations.urls
from profiles.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/register/', register),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^', include(('birds.urls', 'birds'), namespace='birds')),
    url(r'^', include(('profiles.urls', 'profiles'), namespace='profiles')),
    url(r'^', include(('stations.urls', 'stations'), namespace='stations')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
]