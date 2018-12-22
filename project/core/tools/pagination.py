from collections import OrderedDict


from django.utils.translation import ugettext_lazy as _

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import remove_query_param, replace_query_param


class PaginationPermissionsMixin(object):
    """
    Interface for listing permissions in a paginated response.
    """
    def __init__(self, *args, **kwargs):
        self.permissions = None

    def set_permissions(self, permissions):
        self.permissions = permissions


class LinksPageNumberPagination(PaginationPermissionsMixin, PageNumberPagination):
    """
    Decorates the page number paginagtion with _links for navigation and
    extra properties like total page count, result count, etc.
    """
    # Page size parameter configuration.
    page_size_query_param = 'limit'

    # Page size configuration.
    page_size = 100
    max_page_size = 500

    def __init__(self):
        super(LinksPageNumberPagination, self).__init__()
        self.links = []

    def add_link(self, link):
        self.links.append(link)

    def get_paginated_response(self, data):
        content = [
            ('_links', OrderedDict([
                ('first', self.get_first_link()),
                ('last', self.get_last_link()),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link()),
            ] + self.links))
        ]
        if self.permissions:
            content.append(('_permissions', self.permissions))
        content.append(('count', self.page.paginator.count))
        content.append(('pages', self.page.paginator.num_pages))
        content.append(('current_page', self.page.number))
        content.append(('per_page', self.page.paginator.per_page))
        content.append(('results', data))
        return Response(OrderedDict(content))

    def get_first_link(self):
        url = self.request.build_absolute_uri()
        return remove_query_param(url, self.page_query_param)

    def get_last_link(self):
        page_count = self.page.paginator.num_pages
        if not page_count > 1:
            return self.get_first_link()
        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, page_count)

    def paginate_queryset(self, queryset, request, view=None):
        # Skip pagination when csv export is requested
        if request.GET.get('format', '') == 'csv':
            return None

        return super(LinksPageNumberPagination, self).paginate_queryset(queryset, request, view)