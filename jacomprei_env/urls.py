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
    path('solicita-compra/',solicita_compras, name="solicita_compra"),
    path('lista-estabelecimentos/',lista_estabelecimentos, name="lista-estabelecimentos"),
    path('lista-departamentos/',lista_departamentos, name="lista-departamentos"),
    path('detalha-estabelecimentos/<int:nr_item>',detalha_estabeleciemnto, name="detalha-estabelecimentos"),
    path('produtos-por-departamentos/<int:nr_item>',produtos_por_departamentos, name="produto-departamento"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
