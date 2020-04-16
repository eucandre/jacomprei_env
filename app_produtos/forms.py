from django import forms
from .models import *
class FormProdutos(forms.ModelForm):
    class Meta:
        model = produtos
        #fields=['estabelecimento_id','departamento',]
        exclude=['nome','cod_barras','unidade','valor']