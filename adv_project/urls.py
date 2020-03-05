from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from rest_framework import routers
from rest_framework.authtoken import views
from adventure.serializers import RoomViewSet

router = routers.DefaultRouter()
router.register("rooms", RoomViewSet)  # rooms is the endpoint name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/', include(router.urls)),
    path('api/adv/', include('adventure.urls')),
    path("api-token-auth/", views.obtain_auth_token)
]

# now have an endpoint of localhost:8000/api/rooms
