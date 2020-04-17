from django import forms
from .models import *

class FormProdutos(forms.ModelForm):
    class Meta:
        model = produtos
        #fields=['estabelecimento_id','departamento',]
        exclude=['nome','cod_barras','unidade','valor']

class FormSolicitacaoProdutos(forms.ModelForm):
    class Meta:
        model = solicita_compra
        exclude=['cliente','valor', 'produtos']
        fields = ['quantidade',]