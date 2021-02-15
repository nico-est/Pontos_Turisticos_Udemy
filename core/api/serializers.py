from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('cidade',)


class PontoTuristicoSerializer(ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'endereco')
