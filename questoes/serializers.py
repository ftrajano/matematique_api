from rest_framework import serializers
from .models import Disciplina, Assunto, Questao

class QuestaoSerializer(serializers.ModelSerializer):
    disciplina_nome = serializers.SerializerMethodField()
    assunto_nome = serializers.SerializerMethodField()

    class Meta:
        model = Questao
        fields = ['id', 'latex_text', 'disciplina_nome', 'assunto_nome', 'ativo']

    def get_disciplina_nome(self, obj):
        return obj.disciplina.nome

    def get_assunto_nome(self, obj):
        return obj.assunto.nome
