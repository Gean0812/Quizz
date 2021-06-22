from django.db import models

# Create your models here.
class Pergunta(models.Model):
    pergunta = models.CharField(max_length=255)
    dificuldade = models.IntegerField(default=1)

    def __str__(self):
        return self.pergunta

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    alternativa = models.CharField(max_length=255)
    isResposta = models.BooleanField(default=False)

    def __str__(self):
        return self.alternativa

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    score = models.IntegerField(default=0)