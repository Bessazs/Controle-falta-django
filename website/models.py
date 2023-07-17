from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Curso(models.Model): 
    codigo = models.CharField(primary_key=True, max_length=6)
    nome = models.CharField(max_length=56)
    credito=models.PositiveSmallIntegerField()


    def __str__(self):
        texto=f'{self.nome.title()} ({self.credito})'
        
        return texto