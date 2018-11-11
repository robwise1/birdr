from rest_framework import routers
from django.conf.urls import include, url

from profiles import api
from tools.shortcuts import api_url


router = routers.SimpleRouter()
router.register(r'profiles', api.UserViewSet, base_name='profile')

urlpatterns = [
    api_url(r'', include(router.urls))
]