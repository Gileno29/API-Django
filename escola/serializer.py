from dataclasses import Field
from pyexpat import model
from rest_framework import serializers
from escola.models import Aluno

class AlunoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields= ['id', 'nome', 'rg']