from django.http import JsonResponse
from . import models
from django.conf import settings

# Create your views here.
def details(request):
    id = request.GET.get("id", "")

    if not id:
        return JsonResponse({"message": "Informe o ID do usuário"})
    
    user = models.CustomUser.objects.all().filter(id=id)
    userJson = list(user.values())[0]
    
    return JsonResponse(userJson)