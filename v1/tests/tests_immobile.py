from rest_framework import status
from rest_framework.test import APITestCase
from v1.serializers import immobile_serializers
from v1.models import Immobile


class TestImmobile(APITestCase):
    url = "/v1/immobiles"

    fixtures = ["../fixtures/initial_data.json"]

    def test_get_immobile(self):
        response = self.client.get(self.url)
        expected_result = [immobile_serializers.ImmobileSerializer(im).data for im in Immobile.objects.all()]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

    def test_show_immobile(self):
        immobile = Immobile.objects.first()
        response = self.client.get(f"{self.url}/{immobile.pk}")
        expected_result = immobile_serializers.ImmobileSerializer(immobile).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

    def test_create_immobile(self):
        immobile_dict = {
            "max_guests": 13867,
            "num_bathroom": 30172,
            "is_pet_friendly": False,
            "cleaning_fee": 0.5189986420595855,
        }

        response = self.client.post(f"{self.url}", data=immobile_dict)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        immobile_dict["id"] = response.data["id"]
        immobile_dict["created_at"] = response.data["created_at"]
        immobile_dict["updated_at"] = response.data["updated_at"]
        immobile_dict["code"] = response.data["code"]
        self.assertEqual(response.data, immobile_dict)

    def test_update_immobile(self):
        immobile_dict = {
            "code": "ypsm8HU",
            "max_guests": 13867,
            "num_bathroom": 30172,
            "is_pet_friendly": True,
            "cleaning_fee": 0.5189986420595855,
        }
        immobile = Immobile.objects.first()

        response = self.client.put(f"{self.url}/{immobile.pk}", data=immobile_dict)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        immobile_dict["id"] = response.data["id"]
        immobile_dict["created_at"] = response.data["created_at"]
        immobile_dict["updated_at"] = response.data["updated_at"]
        self.assertEqual(response.data, immobile_dict)

    def test_delete_immobile(self):
        immobile = Immobile.objects.first()
        response = self.client.delete(f"{self.url}/{immobile.pk}")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)