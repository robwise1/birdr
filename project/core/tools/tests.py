import simplejson
from django.test import Client

from profiles.models import User


class FunctionalTestCase(object):
    """
    Base class for all functional test, making requests to API etc.
    """
    def create_user(self, **kwargs):
        user = User(**kwargs)
        user.save()
        return user

    def get_client(self, user=None, **kwargs):
        client = Client(**kwargs)
        if user is not None:
            client.force_login(user)
        return client

    def api_post(self, client, path, data):
        return client.post(path, data=simplejson.dumps(data), content_type='application/json')

    def api_put(self, client, path, data):
        return client.put(path, data=simplejson.dumps(data), content_type='application/json')

    def api_patch(self, client, path, data):
        return client.patch(path, data=simplejson.dumps(data), content_type='application/json')
