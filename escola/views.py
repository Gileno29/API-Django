from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerialize

class AlunosViewsSet(viewsets.ModelViewSet):
    queryset= Aluno.objects.all()
    serializer_class= AlunoSerialize