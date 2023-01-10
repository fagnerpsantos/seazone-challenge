from rest_framework import status
from rest_framework.test import APITestCase
from v1.serializers import ad_serializers
from v1.models import Ad


class TestAdvertisement(APITestCase):
    url = "/v1/ads"

    fixtures = ["../fixtures/initial_data.json"]

    def test_get_ad(self):
        response = self.client.get(self.url)
        expected_result = [ad_serializers.AdSerializer(ad).data for ad in Ad.objects.all()]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

    def test_show_ad(self):
        ad = Ad.objects.first()
        response = self.client.get(f"{self.url}/{ad.pk}")
        expected_result = ad_serializers.AdSerializer(ad).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

    def test_create_ad(self):
        ad_dict = {
            "immobile": 5,
            "platform_name": "Listen office worry agency. Evidence do whether partner exactly.",
            "platform_fee": 0.4912685930024243,
        }

        response = self.client.post(f"{self.url}", data=ad_dict)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        ad_dict["id"] = response.data["id"]
        ad_dict["created_at"] = response.data["created_at"]
        ad_dict["updated_at"] = response.data["updated_at"]
        self.assertEqual(response.data, ad_dict)

    def test_update_ad(self):
        ad_dict = {
            "immobile": 5,
            "platform_name": "AirBnb.",
            "platform_fee": 0.4912685930024243,
        }
        ad = Ad.objects.first()

        response = self.client.put(f"{self.url}/{ad.pk}", data=ad_dict)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        ad_dict["id"] = response.data["id"]
        ad_dict["created_at"] = response.data["created_at"]
        ad_dict["updated_at"] = response.data["updated_at"]
        self.assertEqual(response.data, ad_dict)

    def test_dont_allow_delete_ad(self):
        ad = Ad.objects.first()
        response = self.client.delete(f"{self.url}/{ad.pk}")

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)