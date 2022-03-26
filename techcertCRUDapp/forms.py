from socket import fromshare
from django import forms
from .models import Person


# class inherits forms.ModelForm
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'