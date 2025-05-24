from django.urls import path

from request.viewsets.request_viewset import RequestViewset
from request.viewsets.request_info_viewset import RequestInfoViewset

urlspattern = [
    path('request/', RequestViewset.as_view({'post':'create'})),
    path('request/<uuid:pk>', RequestViewset.as_view({'put':'update','get':'list_by_user','delete':'delete'})),
    path('request/info/', RequestInfoViewset.as_view({'post':'create'})),
    path('request/info/<uuid:pk>', RequestInfoViewset.as_view({'put':'update','get':'list_by_request','delete':'delete'})),
]