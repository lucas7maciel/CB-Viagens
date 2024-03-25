from django.urls import path
from . import views

urlpatterns = [
    #GET
    path('', views.search), #Returns a list of trips                | Params (city, date)
    path('cities', views.getCities), #Returns all cities
    #POST
    path('book', views.book) #Associates a trip with a customer     | Params (tripId, customerId)
]