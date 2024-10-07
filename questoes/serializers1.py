from rest_framework import serializers
from .models import Disciplina, Assunto, Questao

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'origem']

class AssuntoSerializer(serializers.ModelSerializer):
    disciplina = DisciplinaSerializer()

    class Meta:
        model = Assunto
        fields = ['id', 'nome', 'disciplina']

class QuestaoSerializer(serializers.ModelSerializer):
    disciplina = DisciplinaSerializer()
    assunto = AssuntoSerializer()

    class Meta:
        model = Questao
        fields = ['id', 'latex_text', 'disciplina', 'assunto', 'ativo']


# Esse serializer cria serializa para um json que contem os campos 
# disciplina e assunto como serializers completos