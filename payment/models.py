from django.db import models

from api.models.base import BaseModel
from rent.models import Rent
from request.models import Request

class PaymentStatus(models.TextChoices):
    AWAITING_PAYMENT = 'Aguardando Pagamento'
    CONCLUDED = 'Concluido'
    CANCELED = 'Cancelado'
    
class PaymentMethod(models.TextChoices):
    MONEY = 'Dinheiro'
    A_VISTA = 'A vista'
    CREDITO = 'Credito'
    PIX = 'PIX'
    
    
class Payment(BaseModel):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, null=True, blank=True)
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, null=True, blank=True)
    method = models.TextField(choices=PaymentMethod.choices)
    total_value = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.TextField(choices=PaymentStatus.choices)
    