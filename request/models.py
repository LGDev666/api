from django.db import models

from api.models.base import BaseModel
from django.contrib.auth.models import User

from book.models import Book

class RequestStatus(models.TextChoices):
    AWAITING_PAYMENT = 'Aguardando Pagamento'
    ON_GOING = 'Em Andamento'
    DELIVERED = 'Entregue'
    CANCELED = 'Cancelado'
    
    
class Request(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.TextField(choices=RequestStatus.choices)
    
class RequestInfo(BaseModel):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=4, decimal_places=2)