from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product

def homepage(request):
    return render(request, 'pages/homepage.html', )


@login_required()
def create(request):
    if request.method == "POST":
        product = Product()
        product.title = request.POST['title']
        product.body = request.POST['body']
        product.url = request.POST['url']
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        product.hunter = request.user
        product.save()
        return redirect('homepage')
    return render(request, 'pages/products/create.html', )
