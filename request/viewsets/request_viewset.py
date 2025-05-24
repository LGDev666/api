from api.viewset.base_viewset import BaseViewset

from rest_framework import pagination, status
from rest_framework.response import Response

from request.models import Request
from request.serializers.request_serializer import RequestSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class RequestViewset(BaseViewset):
    queryset = Request.objects.all()
    serializer = RequestSerializer
    paginator = CustomPagination
    
    def list_by_user(self, request, pk):
        queryset = self.get_queryset()
        paginator = self.get_pagination()
        paginated_qs = paginator.paginate_queryset(queryset.filter(user__id=pk), request)
        serializer = self.get_serializer()(paginated_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        