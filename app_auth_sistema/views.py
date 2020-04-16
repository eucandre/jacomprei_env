# -*- coding: utf-8 -*-
# coding=utf-8
from django.views.generic import CreateView
#from django.core.urlresolvers import reverse_lazy
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm




# class RegistrationView(UserCreationForm):
#   form_class = CustomUserCreationForm
#   success_url = reverse_lazy('register')
#   template_name = "registration/index.html"
#

@login_required()
def registra(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Salvo com sucesso!')
      return redirect("/dash/")
  else:
    form = CustomUserCreationForm()
  return render(request, "registration/index.html", {'form':form})

@login_required()
def muda_sernha(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)  # Important!
      messages.success(request, 'Your password was successfully updated!')
      return redirect('change_password')
    else:
      messages.error(request, 'Please correct the error below.')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'accounts/change_password.html', {
    'form': form
  })
