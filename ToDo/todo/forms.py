from django import forms
from django.forms import ModelForm
from todo.models import ListEntry


class CreateForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = ListEntry
        exclude = ['Id', 'isDone']


class EditForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = ListEntry
        exclude = ['Id']
