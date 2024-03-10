from django.urls import path

from users.views import GetDriverLocation

urlpatterns = [
    path('get-driver/', GetDriverLocation.as_view(), name='get_driver_location')
]
