from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def sign_in(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'], )
        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'pages/accounts/sign_in.html', {'error': 'username or password is incorrect'})
    return render(request, 'pages/accounts/sign_in.html')


def sign_up(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'pages/accounts/sign_up.html', {'error': 'username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password2'])
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'pages/accounts/sign_up.html', {'error': 'Password must match'})

    return render(request, 'pages/accounts/sign_up.html')


def sign_out(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('homepage')

