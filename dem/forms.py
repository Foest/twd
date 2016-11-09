from django import forms
from dem.models import DemUser
from django.contrib.auth.models import User
from localflavor.us.models import USStateField

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {'username', 'email', 'password'}

class DemUserForm(forms.ModelForm):
    state = USStateField(null=True, blank=True)

    class Meta:
        model = DemUser
        fields = {'state'}
