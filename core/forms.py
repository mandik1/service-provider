from django import forms
from .models import  Services,Appointement
from django.forms import ModelForm


class Appointmentform(ModelForm):
    
    class Meta:
        model = Appointement
        fields = ('service','when','address')


# class SearchForm(forms.Form):
#     query = forms.CharField()
