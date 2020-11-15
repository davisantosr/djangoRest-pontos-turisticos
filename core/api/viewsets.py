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
    return PontoTuristico.objects.filter(aprovado=True)

# ## Sobrescrevendo o Método List - Comportamento padrão
# #  de listar os objetos
#   def list(self, request, *args, **kwargs):
#     return Response({"obj":"Sou o obj"})

# def create(self, request, *args, **kwargs):
#   return Response({'Hello': request.data['user']}) #Na requisição é passado um objeto com chave 'user'

# def destroy(self, request, *args, **kwargs):
#   pass

  def retrieve(self, request, *args, **kwargs):
    pass

  def update(self, request, *args, **kwargs): #PUT
    pass

  def partial_update(self, request, *args, **kwargs): #PATCH
    pass

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
  @action(methods=['get'], detail=False)
  def teste(self, request):
    pass
