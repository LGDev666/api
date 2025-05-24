from django.urls import path

from book.viewsets.book_viewset import BookViewset
from book.viewsets.stock_viewset import StockVieset

urlspattern = [
    path('books/', BookViewset.as_view({'get':'list', 'post':'create'})),
    path('book/<uuid:pk>', BookViewset.as_view({'put':'update','get':'get_one','delete':'delete'})),
    path('book/<uuid:pk>/stock', StockVieset.as_view({'get': 'get_quantity'})),
    path('book/<uuid:pk>/stock/add', StockVieset.as_view({'post': 'add_stock'})),
    path('book/<uuid:pk>/stock/remove', StockVieset.as_view({'post': 'remove_stock'})),
]