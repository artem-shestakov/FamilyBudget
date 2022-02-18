from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from . import models

class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('email',)
    
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        # Check to see if any users already exist with this email as a username.
        try:
            match = models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

class NewUserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = '__all__'
