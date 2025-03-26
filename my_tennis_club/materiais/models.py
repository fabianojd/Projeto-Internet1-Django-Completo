from django.db import models

class Materiais(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=20, null=True, blank=True)
    inclusao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Material"            # Nome no singular
        verbose_name_plural = "Materiais"    # Nome correto no plural

    def __str__(self):
        return self.nome
