from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .models import *
import csv, io
from django.contrib import messages
from .forms import *
import random
from django.core.exceptions import ObjectDoesNotExist

def apresentacao(request):
    ids = []
    for i in produtos.objects.all():
        if i.id:
            ids.append(i.id)
    item1 = produtos.objects.get(pk=ids[0])
    item2 = produtos.objects.get(pk=ids[1])
    item3 = produtos.objects.get(pk=ids[2])
    depts = departamentos.objects.all()
    item_objetos = produtos.objects.all().order_by('?')[:4]
    item_atividades = atividades.objects.all().order_by('?')[:4]
    return render(request, 'apresentacao/index.html',
                  {'item2':item2, 'item1':item1,
                   'item3':item3, 'departamentos':depts,
                   'produtos':item_objetos,
                   'atividades':item_atividades})

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = produtos
    template_name = 'busca/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = produtos.objects.filter(
            Q(nome__icontains=query) | Q(departamento__nome__contains=query) | Q(estabelecimento_id__nome__contains=query)
        )
        return object_list

def produto_upload(request):
    template = 'produtos_upload.html'
    data = produtos.objects.all()
    prompt = {'order':'A ordem do csv pode ser : nome, cod_barras, unidade, valor, departamento',
              'produto':data}
    if request.method == 'GET':
        return render(request, template,prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Envie um arquivo csv, este não é válido!')

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    form = FormProdutos(request.POST)

    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        x = column[3].replace('"','')
        created = produtos.objects.update_or_create(
            estabelecimento_id_id = 1,
            departamento_id=1,
            cod_barras = column[0],
            nome= column[1],
            unidade = column[2],
            valor = x
            #departamento = column[4]
        )
    context = {}
    return render(request, template, context)


def lista_estabelecimentos(request):
    try:
        item = estabelecimento.objects.all()
        return render(request, 'app_produtos/lista-estabelecimentos.html',{'item':item})
    except estabelecimento.DoesNotExist:
        raise('Não existe!')

def detalha_estabeleciemnto(request, nr_item):
    try:
        item = estabelecimento.objects.get(pk = nr_item)
        item_objetos = produtos.objects.all().filter(estabelecimento_id=item).order_by('?')[:4]
        return render(request, 'app_produtos/detalha-estabelecimento.html',{'item':item, 'objetos':item_objetos})
    except estabelecimento.DoesNotExist:
        raise ('Não existe!')

def comprar(request,nr_item, id_loja):
    try:
        if request.method == 'POST':
            form = FormSolicitacaoProdutos(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.produtos = request.GET.get('form.produtos')
                item.cliente = request.user
                item.valor = form.quantidade*item.produtos.count()
                item.save()
        else:
            form = FormSolicitacaoProdutos()
            loja = estabelecimento.objects.get(pk = id_loja)
            item_produto = produtos.objects.filter(estabelecimento_id=id_loja).get(pk=nr_item)
            return render(request, 'app_produtos/solicita-compra.html',{'item':item_produto, 'loja':loja, 'form':form})
    except ObjectDoesNotExist:
        raise Http404("Não existe")

def comprar_dois(request,nr_item,nr_item2):
    try:
        item_produto = produtos.objects.get(pk = nr_item)
        item_produto2 = produtos.objects.get(pk=nr_item2)
        return render(request, 'app_produtos/solicita-compra.html',{'item':item_produto, 'item2':item_produto2})
    except ObjectDoesNotExist:
        raise Http404("Não existe")

def comprar_tres(request,nr_item,nr_item2,nr_item3):
    try:
        item_produto = produtos.objects.get(pk = nr_item)
        item_produto2 = produtos.objects.get(pk=nr_item2)
        return render(request, 'app_produtos/solicita-compra.html',{'item':item_produto, 'item2':item_produto2})
    except ObjectDoesNotExist:
        raise Http404("Não existe")

def comprar_quatro(request,nr_item,nr_item2,nr_item3, nr_item4):
    try:
        item_produto = produtos.objects.get(pk = nr_item)
        item_produto2 = produtos.objects.get(pk=nr_item2)
        return render(request, 'app_produtos/solicita-compra.html',{'item':item_produto, 'item2':item_produto2})
    except ObjectDoesNotExist:
        raise Http404("Não existe")

def comprar_cinco(request,nr_item,nr_item2,nr_item3, nr_item4, nr_item5):
    try:
        item_produto = produtos.objects.get(pk = nr_item)
        item_produto2 = produtos.objects.get(pk=nr_item2)
        return render(request, 'app_produtos/solicita-compra.html',{'item':item_produto, 'item2':item_produto2})
    except ObjectDoesNotExist:
        raise Http404("Não existe")


def produtos_por_departamentos_da_loja(request, nr_item):
    try:
        loja = estabelecimento.objects.get(pk = nr_item)
        departamento = departamentos.objects.get(pk = nr_item)
        item = produtos.objects.all().filter(estabelecimento_id__nome=loja.nome, departamento_id=departamento.id)

        return render (request, 'app_produtos/produtos-departamento-loja.html',{'item':item,'loja':loja,'dept':departamento})
    except produtos.DoesNotExist:
        raise ('Não existe!')

def lista_departamentos(request):
    try:
        item = departamentos.objects.all()
        return render (request, 'app_produtos/lista-departamentos.html',{'item':item})
    except produtos.DoesNotExist:
        raise ('Não existe!')

def lista_autonomos_atividade(request, nr_item):
    try:
        item = autonomos.objects.all().filter(atividade_id=nr_item)
        atv = atividades.objects.get(pk=nr_item)
        return render (request, 'app_produtos/lista-autonomos-atividade.html',{'item':item,'atividade':atv})
    except produtos.DoesNotExist:
        raise ('Não existe!')


def detalha_autonomo(request, nr_item):
    try:
        item = autonomos.objects.get(pk = nr_item)
        return render(request, 'app_produtos/detalha-autonomo.html',{'item':item})
    except autonomos.DoesNotExist:
        raise ('Não existe!')

def lista_lojas_por_departamento(request, nm_item):
    try:
        item = estabelecimento.objects.all().filter(obj_depto__nome__contains=nm_item)
        return render(request, 'app_produtos/lists-de-lojas-por-departamento.html',{'item':item})
    except autonomos.DoesNotExist:
        raise ('Não existe!')
