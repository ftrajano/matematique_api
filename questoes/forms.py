from django import forms
from .models import Questao, Assunto, Disciplina



class QuestaoForm(forms.ModelForm):
	class Meta:
		model = Questao
		fields = ('disciplina', 'assunto', 'latex_text', 'math_jax', 'gabarito', 'imagem', 'link_imagem', 'link_bucket')



class AssuntoForm(forms.ModelForm):
	class Meta:
		model = Assunto
		fields = ('nome', 'disciplina')



class DisciplinaForm(forms.ModelForm):
	class Meta:
		model = Disciplina
		fields = ('nome', 'origem')

