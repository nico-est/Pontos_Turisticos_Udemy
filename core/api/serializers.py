from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado')
