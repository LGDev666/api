from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('', include('payment.urls')),
    path('', include('rent.urls')),
    path('', include('request.urls')),
]
