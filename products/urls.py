from django.urls import path
from products.views import create, detail, upvote

urlpatterns = [
    path('create', create, name='create'),
    path('detail/<int:product_id>', detail, name='detail'),
    path('detail/<int:product_id>/upvote', upvote, name='upvote')
]
