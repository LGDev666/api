from uuid import uuid4
from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    
    class Meta:
        abstract = True
