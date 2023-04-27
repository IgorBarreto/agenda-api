from rest_framework import serializers
from .models import Contato


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = [
            'id',
            'nome',
            'sobrenome',
            'nome_completo',
            'foto_contato',
            'telefone',
            'email',
            'endereco',
            'tipo_telefone',
            'data_de_criacao',
            'data_de_atualizacao',
        ]

    data_de_criacao = serializers.DateTimeField(
        source='dt_criacao', read_only=True
    )
    data_de_atualizacao = serializers.DateTimeField(
        source='dt_atualizacao', read_only=True
    )

    def _nome_completo(self, contato):
        return f'{contato.nome} {contato.sobrenome}'

    nome_completo = serializers.SerializerMethodField(
        method_name='_nome_completo', read_only=True
    )

    # def validate(self, attrs):
    #     return super().validate(attrs)

    def validate_telefone(self, value):
        value = ''.join(filter(str.isdigit, value))
        return value
