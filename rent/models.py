from django.db import models

from api.models.base import BaseModel
from django.contrib.auth.models import User

from book.models import Book

class RentStatus(models.TextChoices):
    AWAITING_PAYMENT = 'Aguardando Pagamento'
    ON_GOING = 'Em Andamento'
    DELIVERED = 'Entregue'
    CANCELED = 'Cancelado'
    
class Rent(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rent_start = models.DateTimeField()
    rent_end = models.DateTimeField()
    total_value =  models.DecimalField(max_digits=4, decimal_places=2)
    status = models.TextField(choices=RentStatus.choices)
