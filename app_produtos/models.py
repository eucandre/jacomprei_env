from django.db import models
from app_auth_sistema.models import *

TIPO_PRODUTO = (('bebida alcoolica','bebida_alcoolica'),('bebida sem alcool','bebida_sem_alcool'),
                ('acucares', 'acucares'),('sais','sais'),('salgados','salgados'),('doces','doces')
                , ('combustiveis', 'combustiveis'),('vestuario','vestuario'),('calcados','calcados')
                , ('acessorios_vestimenta', 'acessorios_vestimenta'),('tintas','tintas'),
                ('perfumaria','perfumaria'), ('cama','cama'),('mesa','mesa'),('banho','banho')
                ,('legumes','legumes'),('graos','graos'),('carnes','carnes'),('paes','paes'),
                ('massas','massas'),('eletrodomesticos','eletrodomesticos'),('eletronicos','eletronicos')
                )

UNIDADE_MEDIDA = (('unidade','unidade'),('duzia','duzia'),('ml','ml'),('litro','litro'),('galao','galao')
                  , ('kg', 'kg'),('cento','cento'),('mileiro','mileiro'),('caixa','caixa'),('pacote','pacote')
                  , ('arrouba', 'arrouba'))

PORTE = (('pequeno','pequeno'),('medio','medio'),('grande','grande'))


class departamentos(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.FileField(upload_to="departamento")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Departamentos das lojas'

class estabelecimento(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=23, unique=True)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    porte = models.CharField(max_length=10, choices=PORTE)
    responsavel = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Estabelecimentos'


class produtos(models.Model):
    nome = models.CharField(max_length=255)
    cod_barras = models.CharField(max_length=14)
    imagem = models.FileField(upload_to="produto")
    #tipo_de_produto = models.CharField(max_length=255, choices=TIPO_PRODUTO)
    departamento = models.ForeignKey(departamentos, on_delete=models.CASCADE)
    unidade = models.CharField(max_length=20,choices=UNIDADE_MEDIDA)
    valor = models.CharField(max_length=5)
    estabelecimento_id = models.ForeignKey(estabelecimento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Produtos cadastrados'


# class responsavel_estabelecimento(models.Model):
#     responsavel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     estabelecimento_id = models.ForeignKey(estabelecimento,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.responsavel.nome
#
#     class Meta:
#         verbose_name_plural = 'Responsável por estabelecimentos'
#         unique_together = ['responsavel','estabelecimento_id']
#
#
