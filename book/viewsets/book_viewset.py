from api.viewset.base_viewset import BaseViewset

from rest_framework import pagination

from book.models import Book
from book.serializers.book_serializer import BookSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookViewset(BaseViewset):
    queryset = Book.objects.all()
    serializer = BookSerializer
    paginator = CustomPagination
        
