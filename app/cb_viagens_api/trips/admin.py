from django.contrib import admin
from .models import Trip

class TripAdmin(admin.ModelAdmin):
    # Sets model's fields that can be changed through admin's interface
    list_display = ['id', 'name', 'price_confort', 'price_econ', 'city', 'duration', 'seat', 'bed']


admin.site.register(Trip, TripAdmin)
