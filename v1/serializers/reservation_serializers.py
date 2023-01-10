from rest_framework import serializers
from ..models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        if data['checkin_date'] > data['checkout_date']:
            raise serializers.ValidationError({"checkin_date": "checkin date cannot be later than checkout date"})
        return data
