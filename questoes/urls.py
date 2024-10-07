from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
	QuestaoAPIView, 
	QuestoesAPIView,
	QuestaoViewSet
)

router = SimpleRouter()
router.register('questoes', QuestaoViewSet)

urlpatterns = [
	path('questoes/', QuestoesAPIView.as_view(), name='questoes'),
	path('questoes/<int:pk>', QuestaoAPIView.as_view(), name='questao')
]