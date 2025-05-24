from abc import ABC

from rest_framework import viewsets, status
from rest_framework.response import Response

class BaseViewset(ABC, viewsets.ViewSet):
    queryset = None
    paginator = None
    serializer = None
    
    def get_queryset(self):
        if not self.queryset:
            raise NotImplementedError
        return self.queryset
    
    def get_pagination(self):
        if not self.paginator:
            raise NotImplementedError
        return self.paginator
    
    def get_serializer(self):
        if not self.paginator:
            raise NotImplementedError
        return self.paginator
        
    
    def list(self, request):
        queryset = self.get_queryset()
        paginator = self.get_pagination()
        paginated_qs = paginator.paginate_queryset(queryset.all(), request)
        serializer = self.get_serializer()(paginated_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.get_serializer()(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
    
    def get_one(self, request, pk):
        if not pk:
            return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        queryset = self.get_queryset().filter(id=pk)
        serializer = self.get_serializer()(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        if not pk:
            return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        queryset = self.get_queryset().filter(id=pk)
        serializer = self.get_serializer()(queryset, request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if not pk:
            return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        queryset = self.get_queryset().filter(id=pk)
        queryset.delete()
        return Response('Ok', status=status.HTTP_200_OK)