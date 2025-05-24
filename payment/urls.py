from django.urls import path

from rent.viewsets.rent_viewset import RentViewset

urlspattern = [
    path('payment/', RentViewset.as_view({'post':'create'})),
    path('payment/<uuid:pk>', RentViewset.as_view({'put':'update','get':'list_by_user','delete':'delete'})),
]