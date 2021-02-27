from django.urls import path
from products.views import homepage

urlpatterns = [
    path('', homepage, name='homepage')
]
