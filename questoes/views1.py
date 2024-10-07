from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Questao
from .serializers import QuestaoSerializer

class QuestaoAPIView(APIView):
	"""
	API de Questões do Matematique
	"""
	def get(self, request):
		questoes = Questao.objects.all()
		serializer = QuestaoSerializer(questoes, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = QuestaoSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	