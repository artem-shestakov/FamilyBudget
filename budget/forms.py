from django.forms import ModelForm

from .models import Sources, Savings

class SourceForm(ModelForm):
    class Meta:
        model = Sources
        fields = ['title']

class SavingForm(ModelForm):
    class Meta:
        model = Savings
        fields = [
            'title',
            'amount',
        ]
