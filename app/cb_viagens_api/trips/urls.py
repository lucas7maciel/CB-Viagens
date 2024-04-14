from django.urls import path
from . import views

urlpatterns = [
    #GET
    path('', views.search), # Returns a list of trips                            | Params (city, date)
    path('calculate', views.calculate), # Returns cheapest and quickest trips    | Params (city)
    path('cities', views.getCities), # Returns all cities
    #POST
    path('book/<int:tripId>/<int:userId>/', views.book), # Books trip            | Params (tripId, customerId)
    path('cancel/<int:tripId>/', views.cancel) # Cancels trip                    | Params (tripId)
]