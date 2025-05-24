from django.urls import path

from rent.viewsets.rent_viewset import RentViewset

urlspattern = [
    path('rent/', RentViewset.as_view({'post':'create'})),
    path('rent/<uuid:pk>', RentViewset.as_view({'put':'update','get':'list_by_user','delete':'delete'})),
]