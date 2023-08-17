from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE_SIZE = 10

class CustomPagination(PageNumberPagination):
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size is None:
            return int(self.page_size)
        return int(page_size)

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'page_size': self.get_page_size(self.request),
            'total_page': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
        })
