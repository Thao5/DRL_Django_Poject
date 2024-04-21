from rest_framework.pagination import PageNumberPagination

class DRLPaginator(PageNumberPagination):
    page_size = 3