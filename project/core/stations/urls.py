from rest_framework import routers
from django.conf.urls import include, url

from stations import api
from tools.shortcuts import api_url


router = routers.SimpleRouter()
router.register(r'stations', api.StationViewSet, base_name='station')

urlpatterns = [
    api_url(r'', include(router.urls))
]