# coding=utf-8
import uuid

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from random import choice

class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        cpf = kwargs["cpf"]
        # email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not cpf:
            raise ValueError(_('Usuarios tem que fornecer cpf.'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):

    email = models.EmailField(
        verbose_name=_('Endereco de email'), blank=True, null=True,
    )
    telefone1 = models.CharField(max_length=14, verbose_name=_(u'Telefone para contato'))
    telefone2 = models.CharField(max_length=14, verbose_name=_(u'whatsapp para contato'), null=True, blank=True)

    nome = models.CharField(
        verbose_name=_('Nome'),
        max_length=250,
        blank=False,
        help_text=_('Informe seu nome de usuario'),
    )
    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=14,
        blank=False,
        unique=True,
        help_text=_('Informe seu CPF'),
    )

    rg = models.CharField(
        verbose_name=_('RG'),
        max_length=25,
        blank=False,
        help_text=_('Informe seu CPF'),
    )

    rua = models.CharField(max_length=250, verbose_name=_('Rua'), help_text=_('Informe seu nome da sua rua'))
    bairro = models.CharField(max_length=250, verbose_name=_('Bairro'), help_text=_('Informe seu nome do seu bairro'), )


    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome.__str__()

    def __str__(self):
        if self.nome:
            return self.nome
        else:
            return self.cpf

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'cpf'
    objects = EmailUserManager()


    class Meta:
        verbose_name_plural = 'Usuarios do sistema'

