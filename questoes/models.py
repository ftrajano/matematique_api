from django.db import models

# Create your models here.

class Base(models.Model):
	criacao = models.DateTimeField(auto_now_add=True)
	atualizacao = models.DateTimeField(auto_now=True)
	ativo = models.BooleanField(default=True)

	class Meta:
		abstract = True

class Disciplina(Base):
    ORIGEM_CHOICES = [
        ('PT', 'Exame Nacional Português'),
        ('BR', 'ENEM Brasil'),
        ('SUPERIOR', 'Nível Superior'),
    ]

    nome = models.CharField(max_length=100, unique=True)
    origem = models.CharField(max_length=8, choices=ORIGEM_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.get_origem_display()})"

class Assunto(Base):
    nome = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='assuntos')

    def __str__(self):
        return f"{self.nome} ({self.disciplina.nome})"

class Questao(Base):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)
    latex_text = models.TextField(blank = True, null=True)  # Novo campo para texto em LaTeX
    math_jax = models.TextField(blank = True, null = True) 
    gabarito = models.CharField(max_length = 200)
    dificuldade = models.CharField(max_length = 10, choices=[
        ('FACIL', 'Fácil'),
        ('MEDIO', 'Médio'),
        ('DIFICIL', 'Difícil'),
    ])
    imagem = models.BooleanField(default = False)
    link_imagem = models.URLField(blank =True, null=True)
    link_bucket = models.URLField(blank = True, null=True)

    def __str__(self):
        return self.latex_text
