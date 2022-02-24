from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render

from budget.admin import IncomesAdmin

from . import models

@login_required(login_url='login')
def index(request):
    user = request.user
    user_wallet = user.wallet
    
    context = {'incomes': user_wallet.incomes_set.all()}
    return render(request, 'budget/index.html', context)

@transaction.non_atomic_requests
def create_income(request):
    title = request.POST.get("title")
    user = request.user
    user_wallet = user.wallet
    income = models.Incomes(title=title, wallet=user_wallet)
    income.save()
    return JsonResponse({
        'status': 'created'
    })