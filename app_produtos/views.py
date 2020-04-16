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



def solicita_compras(request):
    if request.method == 'POST':
        form = FormSolicitacaoProdutos(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.cliente = request.user
            item.valor = 0
            for i in form.produtos.valor:
                item.valor = item.valor+i
            item.save()
    else:
        form = FormSolicitacaoProdutos()
    return render(request, 'app_produtos/solicita-compra.html', {'form':form})
