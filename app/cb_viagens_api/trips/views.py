from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from . import models

# Returns a list of trips | Params (city, date)
def search(request):
    # If city or date are not specified, the value will be ''
    # So automatically all values will be returned
    date = request.GET.get('date', '')
    city = request.GET.get('city', '')
    
    queryset = models.Trip.objects.all()

    if city:
        queryset = queryset.filter(city__icontains=city)
    
    if date:
        queryset = queryset.filter(date__icontains=date)

    #Returns response in JSON format
    data = list(queryset.values())
    return JsonResponse(data, status=200, safe=False)


# Returns a list of all available cities trip
def getCities(request):
    queryset = models.Trip.objects.all().values_list('city', flat=True)
    data = list(set(queryset))

    #Returns response in JSON format
    return JsonResponse(data, status=200, safe=False)


# Returns the cheapest and the quickest trip to a desired city
def calculate(request):
    city = request.GET.get('city', '')          # PROGRAMAR CASOS EM QUE VALORES N SÃO ENCONTRADOS

    if not city:
        return JsonResponse({"message": "Please inform a city"})
    
    trips = models.Trip.objects.all().filter(city__icontains=city)
    
    # Cheapest trip
    econPrices = trips.values_list('price_econ', flat=True)
    comfPrices = trips.values_list('price_confort', flat=True)
    
    prices = list(econPrices) + list(comfPrices)
    lowestPrice = min(prices)

    cheapestTripQuery = trips.filter(price_econ=lowestPrice) | trips.filter(price_confort=lowestPrice)
    cheapestTrip = list(cheapestTripQuery.values())[0]

    # Quickest trip
    durationsStr = list(trips.values_list('duration', flat=True))
    durations = [int(x) for x in durationsStr]
    
    quickestTripQuery = trips.filter(duration=min(durations))
    quickestTrip = list(quickestTripQuery.values())[0]

    return JsonResponse({"quickest": quickestTrip, "cheapest": cheapestTrip}, status=200, safe=False)

# Associates a trip record with a customer, changing the 'Customer' field
def book(request, tripId, userId):      # AJEITAR POSSÍVEIS ERROS
    if not tripId or not userId:
        return JsonResponse({"message": "Please inform Trip and User ID"})

    trip = get_object_or_404(models.Trip, pk=tripId)
    user = get_object_or_404(User, pk=userId)

    trip.customer = user
    trip.save()

    return JsonResponse({"message": "Sucesso"})

def cancel(request, tripId):
    if not tripId:
        return JsonResponse({"message": "Please inform trip ID"})
    
    trip = get_object_or_404(models.Trip, pk=tripId)

    trip.customer = None
    trip.save()

    return JsonResponse({"message": "Cancelado"})