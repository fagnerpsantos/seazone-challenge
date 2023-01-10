from rest_framework import viewsets
from ..serializers import immobile_serializers
from ..models import Immobile


class ImmobileViews(viewsets.ModelViewSet):
    serializer_class = immobile_serializers.ImmobileSerializer
    queryset = Immobile.objects.all()
