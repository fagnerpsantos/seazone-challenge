from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from v1.serializers import reservation_serializers
from v1.models import Reservation


class TestReservation(APITestCase):
    url = "/v1/reservations"

    fixtures = ["../fixtures/initial_data.json"]

    def test_get_reservation(self):
        response = self.client.get(self.url)
        expected_result = [reservation_serializers.ReservationSerializer(res).data for res in Reservation.objects.all()]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

    def test_show_reservation(self):
        reservation = Reservation.objects.first()
        response = self.client.get(f"{self.url}/{reservation.pk}")
        expected_result = reservation_serializers.ReservationSerializer(reservation).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

    def test_create_reservation(self):
        reservation_dict = {
            "ad": 5,
            "checkin_date": "1982-08-21",
            "checkout_date": "2011-12-20",
        }

        response = self.client.post(f"{self.url}", data=reservation_dict)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        reservation_dict["id"] = response.data["id"]
        reservation_dict["created_at"] = response.data["created_at"]
        reservation_dict["updated_at"] = response.data["updated_at"]
        reservation_dict["code"] = response.data["code"]
        self.assertEqual(response.data, reservation_dict)

    def test_dont_create_reservation_checkout_date(self):
        reservation_dict = {
            "ad": 5,
            "checkin_date": "2011-12-21",
            "checkout_date": "2011-12-20",
        }

        response = self.client.post(f"{self.url}", data=reservation_dict)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"checkin_date": ["checkin date cannot be later than checkout date"]})

    def test_update_reservation(self):
        reservation_dict = {
            "code": "ypsm8HU",
            "max_guests": 13867,
            "num_bathroom": 30172,
            "is_pet_friendly": True,
            "cleaning_fee": 0.5189986420595855,
        }
        reservation = Reservation.objects.first()

        response = self.client.put(f"{self.url}/{reservation.pk}", data=reservation_dict)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_reservation(self):
        reservation = Reservation.objects.first()
        response = self.client.delete(f"{self.url}/{reservation.pk}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)