from django.db import models
from datetime import datetime

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    empresa = models.CharField(max_length=200)
    data = models.DateTimeField(default=datetime.now, blank=True)
    respondida = models.BooleanField(default=False)

class EmailNewsletter(models.Model):
    email = models.EmailField(max_length=100)
    data = models.DateTimeField(default=datetime.now, blank=True)
    ativo = models.BooleanField(default=True)