from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . import forms


def register_view(request):
    # create form
    form = forms.UserSignUpForm()

    # if register request
    if request.method == 'POST':
        form = forms.UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created")
            return redirect('login')

    context = {
        'form': form
        }
    return render(request, 'users/register.html', context)

def login_view(request):
    # If user signed in go to home page
    if request.user.is_authenticated:
        return redirect('index')
    
    # else go to login page
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Email or login is incorrect')
    context = {}
    return render(request, 'users/login.html', context)

def logout_view(request):
    # logout user
    logout(request)
    return redirect('login')
