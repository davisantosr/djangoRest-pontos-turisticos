from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status 
from rest_framework.decorators import action

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
  serializer_class = PontoTuristicoSerializer

  def get_queryset(self):
    id = self.request.query_params.get('id', None)
    nome = self.request.query_params.get('nome', None)
    descricao = self.request.query_params.get('descricao', None)

    queryset = PontoTuristico.objects.all()

    if id:
      queryset = PontoTuristico.objects.filter(id=id)

    if nome:
      queryset.filter(nome=nome)

    if descricao:
      queryset.filter(descricao=descricao)
    return queryset
# ## Sobrescrevendo o Método List - Comportamento padrão
# #  de listar os objetos
#   def list(self, request, *args, **kwargs):
#     return Response({"obj":"Sou o obj"})

# def create(self, request, *args, **kwargs):
#   return Response({'Hello': request.data['user']}) #Na requisição é passado um objeto com chave 'user'

  def destroy(self, request, *args, **kwargs):
    return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

  def retrieve(self, request, *args, **kwargs):
    return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

  def update(self, request, *args, **kwargs): #PUT
    return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

  def partial_update(self, request, *args, **kwargs): #PATCH
    return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

# Exemplo de implementação de actions personalizadas, usando decorators

# endereço da requisição seria: http://url/pontosturisticos/1/denunciar
  
  # @action(methods=['get', 'post'], detail=True)
  # def denunciar(self, request, pk=None):
  #   print(request.data)
  #   obj = request.data
    
  #   if obj['user'] == 'Usuário1':
  #     return Response('Alright')
  #   else:
  #     return Response('Not allowed')
  
#Exemplo de action para endpoint geral(não apenas para o recurso)
  # @action(methods=['get'], detail=False)
  # def teste(self, request):
  #   pass
