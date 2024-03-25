from django.db import models

# Modelo de viagens
class Trip(models.Model):
    id = models.IntegerField(primary_key=True)
    
    name = models.CharField(max_length=40)
    price_confort = models.CharField(max_length=15)
    price_econ = models.CharField(max_length=15)
    city = models.CharField(max_length=40)
    duration = models.CharField(max_length=10)
    seat = models.CharField(max_length=3)
    bed = models.CharField(max_length=3)

    #A viagem pode estar associada ou nao a um usuario
    customerId = models.IntegerField(blank=True, null=True)
