from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import date

# Modelo de viagens
class Trip(models.Model):
    id = models.IntegerField(primary_key=True)
    
    name = models.CharField(max_length=40)
    price_confort = models.DecimalField(max_digits=10, decimal_places=2)    #CharField(max_length=15)
    price_econ = models.DecimalField(max_digits=10, decimal_places=2)       #CharField(max_length=15)
    city = models.CharField(max_length=40)
    date = models.DateField(default=date.today)
    duration = models.CharField(max_length=10)                              #DecimalField(max_digits=10, decimal_places=2)
    seat = models.CharField(max_length=3)
    bed = models.CharField(max_length=3)

    # A viagem pode estar associada ou nao a um usuario
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
