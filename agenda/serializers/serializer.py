from rest_framework import serializers
from ..models import Contato
from ..validadores import ContatoValidator

# class ContatoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     nome = serializers.CharField(max_length=255)
#     sobrenome = serializers.CharField(max_length=255)
#     nome_completo = serializers.SerializerMethodField()
#     telefone = serializers.CharField(max_length=255)
#     foto_contato = serializers.ImageField()
#     email = serializers.CharField(max_length=255)
#     endereco = serializers.CharField(max_length=255)
#     tipo_telefone = serializers.CharField()
#     data_criacao = serializers.DateTimeField(source ='dt_criacao',read_only=True)
#     data_atualizacao = serializers.DateTimeField(source='dt_atualizacao',read_only=True)
#     def get_nome_completo(self, contato):
#         return f'{contato.nome} {contato.sobrenome}'


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = [
            'id',
            'nome',
            'sobrenome',
            'nome_completo',
            'telefone',
            'foto_contato',
            'email',
            'endereco',
            'tipo_telefone',
            'data_criacao',
            'data_atualizacao',
        ]

    nome_completo = serializers.SerializerMethodField()
    data_criacao = serializers.DateTimeField(
        source='dt_criacao', read_only=True
    )
    data_atualizacao = serializers.DateTimeField(
        source='dt_atualizacao', read_only=True
    )

    def get_nome_completo(self, contato):
        return f'{contato.nome} {contato.sobrenome}'

    def validate_telefone(self, value):
        value = ''.join([v for v in value if str(v).isdigit()])
        return value

    def validate(self, attrs):
        super_validate = super().validate(attrs)
        ContatoValidator(
            data=attrs,
            ErrorClass=serializers.ValidationError,
        )
        return super_validate
