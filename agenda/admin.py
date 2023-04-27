from django.contrib import admin

# Register your models here.
from .models import Contato


class ContatoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Contato, ContatoAdmin)
