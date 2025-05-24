from django.db import models
from api.models.base import BaseModel

class CategoriesChoices(models.TextChoices):
    ROMANCE = "Romance"
    DRAMA = "Drama"

class Book(BaseModel):
    name = models.CharField(max_length=60)
    isbn = models.CharField(max_length=15)
    category = models.TextField(max_length=15, choices=CategoriesChoices.choices)
    writter = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    cover = models.ImageField(upload_to='./book/media/')

    def __str__(self):
        return f"{self.isbn} | {self.name}"
    

class Stock(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def add_book(self):
        self.quantity += 1
        
    def remove_book(self):
        self.quantity -= 1
        