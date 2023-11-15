from django.db import models
from django.contrib.postgres.indexes import HashIndex


class Customer(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField()
