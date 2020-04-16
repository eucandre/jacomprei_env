# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms
from random import choice

from .models import *
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
  nome = forms.CharField(label = 'Nome',max_length = 250,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':u'Nome do Usuário'}))
  cpf =forms.CharField(label='Cpf',max_length=14, widget=forms.TextInput(attrs= {'class':'form-control','placeholder':u'CPF'}))
  rg = forms.CharField(label='RG', max_length=50,required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'RG'}))
  email = forms.EmailField(label ='e-mail' ,required=False,widget = forms.EmailInput(attrs = {'class':'form-control', 'placeholder':u'E-mail'}))
  rua = forms.CharField(label = 'Rua',max_length = 255,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':u'RUA'}))
  bairro = forms.CharField(label = 'Bairro',max_length = 255,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':u'BAIRRO'}))
  #cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(),widget=forms.Select(attrs= {'class':'form-control'}))
  telefone1 = forms.CharField(label='Telefone',max_length= 14,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':u'Telefone'}))
  telefone2 = forms.CharField(label='Whatsapp', max_length=14,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Whatsapp'}))

  class Meta:
    model = MyUser
    fields = ('nome','cpf','rg','email','rua','bairro','telefone1','telefone2','groups')



