from collections import defaultdict

from django.core.exceptions import ValidationError
from .models import Contato


class ContatoValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.Errorclass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()

    def clean(self, *args, **kwargs):
        self.clean_telefone()
        telefone = self.data.get('telefone')
        telefone = Contato.objects.filter(telefone=telefone).first()
        if telefone:
            raise self.Errorclass(
                {'telefone': ['Este campo já foi cadastrado.']}
            )

    def clean_telefone(self):
        value = self.data.get('telefone')
        if value is not None:
            value = ''.join([v for v in value if str(v).isdigit()])
            return value
