from django import forms
from .models import Employeeforms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Magesh(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True)
    mob_no = forms.CharField(max_length=10, required=True)
    email = forms.CharField(max_length=30, required=True)
    job = forms.CharField(max_length=30, required=True)

    class Meta:
        model = Employeeforms
        fields = {'name', 'mob_no', 'email', 'job'}


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
