from django import forms
from .models import Contract, Client

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['monthly_fee', 'effective_date', 'expiry_date', 'client', 'sale']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'effective_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'monthly_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale': forms.NumberInput(attrs={'class': 'form-control'}),
        }