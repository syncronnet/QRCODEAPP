# forms.py

# forms.py

from django import forms
from .models import QRCode

class QRCodeForm(forms.ModelForm):
    salvar_nome = forms.CharField(max_length=100)  # Adicionando o campo salvar_nome

    class Meta:
        model = QRCode
        fields = ['link', 'salvar_nome']  # Adicionando o campo salvar_nome aos campos do formulário

