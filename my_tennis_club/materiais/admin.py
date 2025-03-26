from django.contrib import admin
from .models import Materiais

class MateriaisAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nome", "cor", "inclusao")

admin.site.register(Materiais, MateriaisAdmin)

