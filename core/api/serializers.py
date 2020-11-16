from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
  atracoes = AtracaoSerializer(many=True,)
  descricao_completa = SerializerMethodField()
  
  class Meta:
    model = PontoTuristico
    fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
     'atracoes', 'descricao_completa', 'descricao_completa_complementar',)

  
  def get_descricao_completa(self, obj):
    return '%s - %s' % (obj.nome, obj.descricao)