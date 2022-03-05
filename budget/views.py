from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from budget.admin import IncomesAdmin

from .models import Incomes
from .forms import IncomeForm

@login_required(login_url='login')
def index(request):
    context = {}
    return render(request, 'budget/index.html', context)

@login_required(login_url='login')
def incomes_list(request):
    user = request.user
    user_wallet = user.wallet

    context = {'incomes': user_wallet.incomes_set.all()}
    return render(request, 'budget/income_list.html', context)

@transaction.non_atomic_requests
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.wallet = request.user.wallet
            income.save()
            return HttpResponse(
                status=204,
            )
    else:
        form = IncomeForm()
    return render(request, 'budget/add_income.html', {
        'form': form
    })

@transaction.non_atomic_requests
def edit_income(request, id):
    income = get_object_or_404(Incomes, pk=id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income.save()
            return HttpResponse(
                status=204,
            )
    else:
        form = IncomeForm(instance=income)
    return render(request, 'budget/add_income.html', {
        'form': form,
        'income': income
    })