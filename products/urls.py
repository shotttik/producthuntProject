from django.urls import path
from products.views import create

urlpatterns = [
    path('create', create, name='create')
]
