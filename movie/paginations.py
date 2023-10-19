from rest_framework.pagination import PageNumberPagination,CursorPagination

class GenrePagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 6

class GenreCursorPagination(CursorPagination):
    page_size = 4