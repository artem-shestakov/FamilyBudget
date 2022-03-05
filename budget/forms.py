from dataclasses import fields
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Incomes

class IncomeForm(ModelForm):
    class Meta:
        model = Incomes
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data['title']
        if Incomes.objects.filter(title=title).exists():
            raise ValidationError(f"Income with title {title} already exists")
