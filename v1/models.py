from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.


def generate_code():
    return get_random_string(7)


class Immobile(models.Model):
    code = models.CharField(max_length=7, null=False, blank=False, editable=False, default=generate_code)
    max_guests = models.IntegerField(null=False, blank=False)
    num_bathroom = models.IntegerField(null=False, blank=False)
    is_pet_friendly = models.BooleanField(default=True)
    cleaning_fee = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ad(models.Model):
    immobile = models.ForeignKey(to=Immobile, on_delete=models.CASCADE, null=False, blank=False)
    platform_name = models.CharField(max_length=100, null=False, blank=False)
    platform_fee = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    code = models.CharField(max_length=7, null=False, blank=False, editable=False, default=generate_code)
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE, null=False, blank=False)
    checkin_date = models.DateField(null=False, blank=False)
    checkout_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
