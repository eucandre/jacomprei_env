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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
