from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import SearchStats
from django import forms
import re


def isStandardized(value):
    if not re.compile(r'^[a-zA-Z ]+$').match(value):
        return False
    return True


class AuthorForm(ModelForm):
    """
    Can also do 
    name = forms.CharField(validators=[isStandardized],widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name of an author'}))
    surname = forms.CharField(validators=[isStandardized],widget=forms.TextInput(attrs={'class':'form-control','placeholder':'surname of an author' }))
    """

    class Meta:

        model = SearchStats
        fields = ('name', 'surname', 'author_id', 'amount')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                'placeholder': 'Name of an author'
            }),
            'surname': forms.TextInput(attrs={'class': 'form-control',
                'placeholder': 'Surname of an author'
            }),
            'author_id': forms.TextInput(attrs={'type': 'hidden'}),
            'amount': forms.TextInput(attrs={'type': 'hidden'}),
            }
