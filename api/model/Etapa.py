from django.db import models
from django.utils import timezone

class Etapa(models.Model):
    macro_setor = models.CharField(max_length=20)
    setor = models.CharField(max_length=30)

    def __str__(self):
        return self.macro_setor