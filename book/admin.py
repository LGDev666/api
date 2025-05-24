from django.contrib import admin
from book.models import Book

class BookAdmin(admin.ModelAdmin):
    model = Book
    
admin.site.register(Book, BookAdmin)