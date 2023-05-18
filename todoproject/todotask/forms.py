from django import forms

from .models import todo


class task1(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['name', 'priority', 'date']
