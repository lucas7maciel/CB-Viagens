from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, QueryDict
from . import models

# Returns a list of trips | Params (city, date)
def search(request):
    # If city or date are not specified, the value will be ''
    # So automatically all values will be returned
    date = request.GET.get('date', '')
    city = request.GET.get('city', '')
    
    queryset = models.Trip.objects.filter(city__icontains=city) #date__icontains=date, 
    data = list(queryset.values())

    #Returns response in JSON format
    return JsonResponse(data, status=200, safe=False)


# Returns a list of all available cities trip
def getCities(request):
    queryset = models.Trip.objects.all().values_list('city', flat=True)
    data = list(queryset)

    #Returns response in JSON format
    return JsonResponse(data, status=200, safe=False)


# Associates a trip record with a customer, changing the 'CustomerId' field
@csrf_exempt
def book(request):
    if (request.method != "POST"):
        return JsonResponse({"message": "Use a POST request to book a trip"})
    
    # Will be used to get request params
    put = QueryDict(request.body)

    customerId = put.get("customer_id")
    tripId = put.get("trip_id")

    if customerId is None or tripId is None:
        return JsonResponse({"message": "Params are missing (tripId, customerId)"})

    try:
        # Gets the desired trip
        trip = models.Trip.objects.get(id=tripId)
        trip.update(customerId=customerId)
        trip.save()
        
        return JsonResponse({"message": f"Trip {tripId} succesfully booked for customer {customerId}"})
    except models.Trip.DoesNotExist:
        return JsonResponse({"message": "The desired trip is not available"})
    
