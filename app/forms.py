from django import forms
from django.db.models import fields
from .models import TODO

class Todoform(forms.ModelForm):
    class Meta:
        model = TODO
        exclude = ('user','date')
        widgets = {
            
        }
        