from django.db import models
from phone_field import PhoneField
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField


class Guest(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = USStateField(blank=True)
    zip = USZipCodeField(blank=True)
    email = models.EmailField(max_length=50)
    phone = PhoneField(blank=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
