from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect, render

from budget.admin import IncomesAdmin

from . import models
from .forms import IncomeForm

@login_required(login_url='login')
def index(request):
    user = request.user
    user_wallet = user.wallet
    
    context = {'incomes': user_wallet.incomes_set.all()}
    return render(request, 'budget/index.html', context)

@transaction.non_atomic_requests
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.wallet = request.user.wallet
            income.save()
            return redirect("/")
    else:
        form = IncomeForm()
    return render(request, 'budget/add_income.html', {
        'form': form
    })