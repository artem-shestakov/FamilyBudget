import json
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from budget.admin import SourcesAdmin

from .models import Sources, Savings
from .forms import SourceForm, SavingForm

# Index
@login_required(login_url='login')
def index(request):
    context = {}
    return render(request, 'budget/index.html', context)

@login_required(login_url='login')
def sources_list(request):
    user = request.user
    user_wallet = user.wallet

    context = {'sources': user_wallet.sources_set.all()}
    return render(request, 'budget/source_list.html', context)

# Sources
@login_required(login_url='login')
@transaction.non_atomic_requests
def add_source(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            source = form.save(commit=False)
            source.wallet = request.user.wallet
            source.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'sourceListChange': None,
                        'showMessage': f'Source {source.title} added.'
                    })
                })
    else:
        form = SourceForm()
    return render(request, 'budget/source_form.html', {
        'form': form
    })

@login_required(login_url='login')
@transaction.non_atomic_requests
def edit_source(request, id):
    source = get_object_or_404(Sources, pk=id)
    old_title = source.title
    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            source.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'sourceListChange': None,
                        'showMessage': f'Source {old_title} updated.'
                    })
                })
    else:
        form = SourceForm(instance=source)
    return render(request, 'budget/source_form.html', {
        'form': form,
        'source': source
    })

@login_required(login_url='login')
@transaction.non_atomic_requests
def delete_source(request, id):
    source = get_object_or_404(Sources, pk=id)
    source.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "sourceListChange": None,
                "showMessage": f"Source {source.title} deleted."
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
        form = SavingForm(instance=saving)
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