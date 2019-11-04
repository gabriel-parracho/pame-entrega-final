from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.model.Etapa import Etapa
from api.model.Produto import Produto
from api.serializers import EtapaSerializer, ProdutoSerializer
from django.shortcuts import get_object_or_404

class EtapaList(APIView):
    def get(self,request):
        etapa = Etapa.objects.all()
        data = EtapaSerializer(etapa, many=True).data

        return Response(data)

    def post(self,request):
        macro_setor = request.data ['macro_setor']
        setor = request.data ['setor']
        etapa = Etapa(macro_setor= macro_setor, setor= setor)
        etapa.save()
        data = EtapaSerializer(etapa).data

        return Response(data)
    
class ProdutoList(APIView):
    def post(self, request):
        tipo = request.data['tipo']
        quantidade = request.data['quantidade']
        etapa_id=request.data['etapa_id']

        etapa = get_object_or_404(Etapa, pk=etapa_id)
        inserir = Produto(tipo=tipo, quantidade=quantidade, etapa=etapa)
        inserir.save()
        
        data = ProdutoSerializer(inserir).data

        return Response(data)

class ProdutoDetail(APIView):
    def get(self,request,pk):

        etapa = get_object_or_404(Etapa, pk=pk)

        produto = Produto.objects.filter(etapa=etapa)

        data = ProdutoSerializer(produto, many=True).data

        return Response(data)


# Create your views here.
