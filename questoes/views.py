from rest_framework import generics
from rest_framework import viewsets

"""
	API Versão 1
"""

from .models import Questao
from .serializers import QuestaoSerializer

# class QuestoesAPIView(generics.ListCreateAPIView): 
class QuestoesAPIView(generics.ListAPIView): 
	queryset = Questao.objects.all()
	serializer_class = QuestaoSerializer


class QuestaoAPIView(generics.RetrieveAPIView):
	queryset = Questao.objects.all()
	serializer_class = QuestaoSerializer


"""
	API Versão 2
"""
class QuestaoViewSet(viewsets.ModelViewSet):
	queryset = Questao.objects.all()
	serializer_class = QuestaoSerializer