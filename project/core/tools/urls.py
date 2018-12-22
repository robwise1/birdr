from django import template
from django.conf import settings

from rest_framework.reverse import reverse

register = template.Library()


@register.simple_tag(name='api_url')
def reverse_api(viewname, args=None, kwargs=None, request=None, format=None, serializer=None, **extra):
    kwargs = kwargs or {}

    if 'version' not in kwargs:
        kwargs['version'] = settings.REST_FRAMEWORK['DEFAULT_VERSION']

    if not request and serializer:
        request = serializer.context['request']

    if not format and serializer:
        format = serializer.context['format']

    return reverse(viewname, args=args, kwargs=kwargs, request=request, format=format, **extra)