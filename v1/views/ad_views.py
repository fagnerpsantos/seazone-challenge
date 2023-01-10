from rest_framework import viewsets
from ..serializers import ad_serializers
from ..models import Ad


class AdViews(viewsets.ModelViewSet):
    serializer_class = ad_serializers.AdSerializer
    queryset = Ad.objects.all()
