from django.urls import path
from api.views import EtapaList, ProdutoList, ProdutoDetail

urlpatterns = [
    path('etapa/', EtapaList.as_view()),
    path('etapa/produto/', ProdutoList.as_view()),
    path('etapa/produto/<int:pk>', ProdutoDetail.as_view())
]