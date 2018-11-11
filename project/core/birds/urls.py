from rest_framework import routers
from django.conf.urls import include, url

from birds import api
from tools.shortcuts import api_url


router = routers.SimpleRouter()
router.register(r'birds', api.BirdViewSet, base_name='bird')

urlpatterns = [
    api_url(r'', include(router.urls))
]