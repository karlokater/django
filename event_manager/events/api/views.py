from events import models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer, EventSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Implementiert alle nötigen Endpunkte."""
    serializer_class = CategorySerializer
    queryset = models.Category.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """Implementiert alle nötigen Endpunkte."""
    serializer_class = EventSerializer
    queryset = models.Event.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
