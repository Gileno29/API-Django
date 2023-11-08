from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)

    def __str__(self):
        return self.nome
    

class Professor(models.Model):
    Nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    matricula=models.IntegerField(max_length=20)