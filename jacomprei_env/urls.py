from django.contrib import admin
from django.urls import path
from app_produtos.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',apresentacao),
    #path('', HomePageView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('produto_upload/', produto_upload, name="produto_upoad"),
    path('solicita-compra/<int:nr_item>/<int:id_loja>',comprar, name="solicita_compra"),
    path('lista-estabelecimentos/',lista_estabelecimentos, name="lista-estabelecimentos"),
    path('lista-departamentos/',lista_departamentos, name="lista-departamentos"),
    path('detalha-estabelecimentos/<int:nr_item>',detalha_estabeleciemnto, name="detalha-estabelecimentos"),
    #path('produtos-por-departamentos/<int:nr_item>',produtos_por_departamentos, name="produto-departamento"),
    path('produtos-por-departamento-loja/<int:nr_item>', produtos_por_departamentos_da_loja, name="produtos-por-departamento-loja"),
    path('lojas-por-departamento/<str:nm_item>',lista_lojas_por_departamento, name="lista-lojas-departamento"),
    path('autonomos-por-atividade/<int:nr_item>',lista_autonomos_atividade, name="autonomos-atividade"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
