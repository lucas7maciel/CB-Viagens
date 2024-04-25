
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin's interface
    #path('admin/', admin.site.urls),
    # Trips routes
    path('trips/', include('trips.urls')),
    # Authentication routes
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('users.urls'))
]
