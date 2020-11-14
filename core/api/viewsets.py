from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
  serializer_class = PontoTuristicoSerializer

  def get_queryset(self):
    return PontoTuristico.objects.filter(aprovado=True)

## Sobrescrevendo o Método List - Comportamento padrão
#  de listar os objetos
  def list(self, request, *args, **kwargs):
    return Response({"obj":"Sou o obj"})