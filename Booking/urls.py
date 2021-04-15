from django.urls import path
from .views import reservation


urlpatterns = [
    path('/', reservation, name='booking')
]