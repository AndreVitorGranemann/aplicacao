from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id','nome', 'email')
    list_display_link =('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 1


admin.site.register(Pessoa, ListandoPessoas)

