from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from . import forms


def registerPage(request):
    form = forms.UserSignUpForm()

    if request.method == 'POST':
        form = forms.UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {
        'form': form
        }
    return render(request, 'users/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'users/login.html', context)
