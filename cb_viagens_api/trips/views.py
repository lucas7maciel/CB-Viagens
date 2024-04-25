from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from users.models import CustomUser
from . import models

# Returns a list of trips | Params (city, date)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request):
    # If city or date are not specified, the value will be ''
    # So automatically all values will be returned
    date = request.GET.get('date', '')
    city = request.GET.get('city', '')
    
    queryset = models.Trip.objects.all().filter(customer=None) # Setar essa propriedade pra outras views

    if city:
        queryset = queryset.filter(city__icontains=city)
    
    if date:
        queryset = queryset.filter(date__icontains=date)

    #Returns response in JSON format
    data = list(queryset.values())
    return JsonResponse(data, status=200, safe=False)


# Returns a list of all available cities trip
def getCities(request):
    queryset = models.Trip.objects.all().filter(customer=None).values_list('city', flat=True)
    data = list(set(queryset))

    #Returns response in JSON format
    return JsonResponse(data, status=200, safe=False)


# Returns the cheapest and the quickest trip to a desired city
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calculate(request):
    city = request.GET.get('city', '')

    if not city:
        return JsonResponse({"message": "Informe a cidade"})
    
    # Colocar aqui pra informar a dara
    
    trips = models.Trip.objects.all().filter(customer=None).filter(city__icontains=city)
    
    # Cheapest trip
    econPrices = trips.values_list('price_econ', flat=True)
    comfPrices = trips.values_list('price_confort', flat=True)
    
    prices = list(econPrices) + list(comfPrices)
    lowestPrice = min(prices)

    cheapestTripQuery = trips.filter(price_econ=lowestPrice) | trips.filter(price_confort=lowestPrice)
    cheapestTrip = list(cheapestTripQuery.values())[0]

    # Quickest trip
    quickestTripQuery = trips.order_by('duration')
    quickestTrip = list(quickestTripQuery.values())[0]

    return JsonResponse({"quickest": quickestTrip, "cheapest": cheapestTrip}, status=200, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBooked(request, id):
    if not id:
        return JsonResponse({"message": "Please provide Id"})
    
    tripsQuery = models.Trip.objects.all().filter(customer=id)
    trips = list(tripsQuery.values())

    return JsonResponse(trips, safe=False)

# Associates a trip record with a customer, changing the 'Customer' field
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book(request, tripId, userId):
    if not tripId or not userId:
        return JsonResponse({"message": "Please inform Trip and User ID"})

    try:
        user = get_object_or_404(CustomUser, pk=userId)
    except Http404:
        return JsonResponse({"message": "Usuário não encontrado"})

    try:
        trip = get_object_or_404(models.Trip, pk=tripId)
    except Http404:
        return JsonResponse({"message": "Viagem não encontrada"})

    if trip.customer is not None:
        if trip.customer.id == userId:
            return JsonResponse({"message": "Você já reservou esta viagem"})
        
        return JsonResponse({"message": "Viagem já reservada"})

    trip.customer = user
    trip.save()

    return JsonResponse({"success": "Viagem reservada com sucesso"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cancel(request, tripId):
    if tripId is None:
        return JsonResponse({"message": "Informe o ID da viagem"})
    
    try:
        trip = get_object_or_404(models.Trip, pk=tripId)
    except Http404:
        return JsonResponse({"message": "Viagem não encontrada"})
    
    if trip.customer is None:
        return JsonResponse({"message": "Viagem já cancelada"})

    trip.customer = None
    trip.save()

    return JsonResponse({"success": "Viagem cancelada com sucesso"})