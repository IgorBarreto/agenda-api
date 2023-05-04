from django.db import models


# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    foto_contato = models.ImageField(upload_to='agenda/contatos/', blank=True)
    email = models.CharField(
        max_length=255, unique=True, blank=False, null=False
    )
    endereco = models.CharField(max_length=255)
    TELEFONE_CHOICES = (
        ('Trabalho', 'Trabalho'),
        ('Celular', 'Celular'),
        ('Casa', 'Casa'),
    )
    tipo_telefone = models.CharField(
        max_length=50,
        choices=TELEFONE_CHOICES,
        blank=False,
        null=False,
        default='Celular',
    )
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(f'{self.nome} {self.sobrenome}')
