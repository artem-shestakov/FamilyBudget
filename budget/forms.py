from django.forms import ModelForm

from .models import Source, Saving

class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = ['title']

class SavingForm(ModelForm):
    class Meta:
        model = Saving
        fields = [
            'title',
            'amount',
        ]
