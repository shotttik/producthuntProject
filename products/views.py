from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product


def homepage(request):
    products = Product.objects.all()
    return render(request, 'pages/homepage.html', {'products': products})


@login_required(login_url="/accounts/signup")
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
        return redirect('/products/detail/' + str(product.id))
    return render(request, 'pages/products/create.html', )


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pages/products/detail.html', {'product': product})


@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()   # ცვლის იმ პროდუქტის ინფოს ბაზაში რომელსაც upvote-ს ვაძლევთ
        return redirect('/products/detail/' + str(product.id))
