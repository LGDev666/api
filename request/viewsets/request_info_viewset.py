from api.viewset.base_viewset import BaseViewset

from rest_framework import pagination, status
from rest_framework.response import Response

from request.models import Request
from request.serializers.request_serializer import RequestSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class RequestInfoViewset(BaseViewset):
    queryset = Request.objects.all()
    serializer = RequestSerializer
    paginator = CustomPagination
    
    def list_by_request(self, request, pk):
        queryset = self.get_queryset()
        serializer = self.get_serializer()(queryset.filter(user__id=pk), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        