from rest_framework.serializers import ModelSerializer

from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
  atracoes = AtracaoSerializer(many=True,)

  class Meta:
    model = PontoTuristico
    fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes',)