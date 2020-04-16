from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .models import *
import csv, io
from django.contrib import messages
from .forms import *

def apresentacao(request):
    # item3 = produtos.objects.all()[(len(produtos.objects.all())-3):]
    # item2 = produtos.objects.all()[(len(produtos.objects.all()) - 2):]
    # item1 = produtos.objects.all()[(len(produtos.objects.all()) - 1):]
    tamanho_produtos = len(produtos.objects.all())
    if tamanho_produtos == 1:
        item = produtos.objects.get(pk = (len(produtos.objects.all())))
        return render(request, 'apresentacao/index.html', {'item': item})
    item_departamento = departamentos.objects.all()
    item2 = produtos.objects.get(pk=(len(produtos.objects.all())) - 2)
    item1 = produtos.objects.get(pk=(len(produtos.objects.all())) - 1)
    return render(request, 'apresentacao/index.html', {'item2':item2, 'item1':item1})

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
            estabelecimento_id_id = form.estabelecimento_id,
            departamento_id=form.departamento,
            cod_barras = column[0],
            nome= column[1],
            unidade = column[2],
            valor = x.replace(',','.'),
            #departamento = column[4]
        )
    context = {}
    return render(request, template, context)

