from django.db import models
from django.utils import timezone
from api.models import Etapa

class Produto(models.Model):
    tipo = models.CharField(max_length=20)
    quantidade =models.IntegerField(default=0)
    data = models.DateTimeField (default=timezone.now)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo