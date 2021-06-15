from django import forms
from .models import Student


class Check(forms.ModelForm):
    name = forms.CharField(max_length=30,required=True)
    mob_no = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(max_length=30, required=True)
    course = forms.CharField(max_length=30, required=True)

    class Meta:
        model = Student
        fields = {'name', 'mob_no', 'email', 'course'}
