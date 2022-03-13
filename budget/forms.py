from dataclasses import fields
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Incomes, Savings

class IncomeForm(ModelForm):
    class Meta:
        model = Incomes
        fields = ['title']

class SavingForm(ModelForm):
    class Meta:
        model = Savings
        fields = [
            'title',
            
        ]
