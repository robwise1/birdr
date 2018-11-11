from django.conf.urls import url


def api_url(regex, view, **kwargs):
    return url(r'^api/v(?P<version>[0-9]+(\.[0-9])?)/' + regex, view, **kwargs)