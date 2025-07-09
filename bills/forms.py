from django import forms
from .models import Conta

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['titulo', 'descricao', 'valor', 'vencimento', 'pago']