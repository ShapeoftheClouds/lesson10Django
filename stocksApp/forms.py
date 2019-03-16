from django import forms
from .models import Stockspractice

class StockForm(forms.ModelForm):
    class Meta:
        model = Stockspractice
        fields = ['stockname', 'shareno', 'earnings']
        labels = {'text':''}
