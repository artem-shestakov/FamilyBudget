import json
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from budget.admin import IncomesAdmin

from .models import Incomes, Savings
from .forms import IncomeForm, SavingForm

# Index
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

# Incomes
@login_required(login_url='login')
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
                headers={
                    'HX-Trigger': json.dumps({
                        'incomeListChange': None,
                        'showMessage': f'Income {income.title} added.'
                    })
                })
    else:
        form = IncomeForm()
    return render(request, 'budget/income_form.html', {
        'form': form
    })

@login_required(login_url='login')
@transaction.non_atomic_requests
def edit_income(request, id):
    income = get_object_or_404(Incomes, pk=id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'incomeListChange': None,
                        'showMessage': f'Income {income.title} updated.'
                    })
                })
    else:
        form = IncomeForm(instance=income)
    return render(request, 'budget/income_form.html', {
        'form': form,
        'income': income
    })

@login_required(login_url='login')
@transaction.non_atomic_requests
def delete_income(request, id):
    income = get_object_or_404(Incomes, pk=id)
    income.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "incomeListChange": None,
                "showMessage": f"Income {income.title} deleted."
            })
        })

# Savings
@login_required(login_url='login')
def savings_list(request):
    user = request.user
    user_wallet = user.wallet

    context = {'savings': user_wallet.savings_set.all()}
    return render(request, 'budget/saving_list.html', context)

@login_required(login_url='login')
@transaction.non_atomic_requests
def add_saving(request):
    if request.method == 'POST':
        form = SavingForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.wallet = request.user.wallet
            saving.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'savingListChange': None,
                        'showMessage': f'Saving {saving.title} added.'
                    })
                })
    else:
        form = SavingForm()
    return render(request, 'budget/saving_form.html', {
        'form': form
    })

@login_required(login_url='login')
@transaction.non_atomic_requests
def edit_saving(request, id):
    saving = get_object_or_404(Savings, pk=id)
    current_title = saving.title
    if request.method == 'POST':
        form = SavingForm(request.POST, instance=saving)
        if form.is_valid():
            saving.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'savingListChange': None,
                        'showMessage': f'Saving {current_title} was updated.'
                    })
                })
    else:
        form = IncomeForm(instance=saving)
    return render(request, 'budget/saving_form.html', {
        'form': form,
        'saving': saving
    })

@login_required(login_url='login')
@transaction.non_atomic_requests
def delete_saving(request, id):
    saving = get_object_or_404(Savings, pk=id)
    saving.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "savingListChange": None,
                "showMessage": f"Saving {saving.title} was deleted."
            })
        })