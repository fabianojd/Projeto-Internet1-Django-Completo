from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')  # Lista os campos na tabela do admin
    search_fields = ('title',)  # Campo de busca
    list_filter = ('created_at',)  # Filtro lateral por data de criação
    ordering = ('id',)  # Ordenação padrão

    readonly_fields = ('created_at', 'updated_at')  # Apenas leitura para datas

   # admin.site.register(PLan)

