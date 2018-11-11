from rest_framework import routers
from django.conf.urls import include, url

from nets import api
from tools.shortcuts import api_url


router = routers.SimpleRouter()
router.register(r'nets', api.NetViewSet, base_name='net')

urlpatterns = [
    api_url(r'', include(router.urls))
]