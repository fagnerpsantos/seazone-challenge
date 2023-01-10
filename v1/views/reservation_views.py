from rest_framework import viewsets
from ..serializers import reservation_serializers
from ..models import Reservation


class ReservationViews(viewsets.ModelViewSet):
    serializer_class = reservation_serializers.ReservationSerializer
    queryset = Reservation.objects.all()
