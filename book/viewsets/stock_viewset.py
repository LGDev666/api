from rest_framework import viewsets, status
from rest_framework.response import Response

from book.serializers.stock_serializer import StockSerializer

from book.models import Stock

class StockVieset(viewsets.ViewSet):
    queryset = Stock.objects.all()
    serializer = StockSerializer
    
    def add_stock(self, request, pk):
        if not pk: 
            return Response('Bad Resquest', status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.queryset.get(book__id=pk)
        if queryset:
            queryset.add_book()
            return Response('Added', status=status.HTTP_200_OK)
        return Response('Bad Resquest', status=status.HTTP_400_BAD_REQUEST)
        
    def remove_stock(self, request, pk):
        if not pk: 
            return Response('Bad Resquest', status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.queryset.get(book__id=pk)
        if queryset:
            queryset.remove_book()
            return Response('Removed', status=status.HTTP_200_OK)
        return Response('Bad Resquest', status=status.HTTP_400_BAD_REQUEST)
    
    def get_quantity(self, request, pk):
        if not pk: 
            return Response('Bad Resquest', status=status.HTTP_400_BAD_REQUEST)
    
        queryset = self.queryset.get(book__id=pk)
        
        if queryset:
            return Response(queryset.quantity, status=status.HTTP_200_OK)
        return Response('Bad Resquest', status=status.HTTP_400_BAD_REQUEST)