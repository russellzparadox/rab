from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from users.models import Driver
from users.serializers import DriverLocation


# Create your views here.

class GetDriverLocation(GenericAPIView):
    # permission_classes = (IsUnauthorized,)
    serializer_class = DriverLocation

    # @staticmethod
    # def post(request, *args, **kwargs):
    #     serializer = PhoneStatusSerializer(data=request.data)
    #     if serializer.is_valid():
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @staticmethod
    def get(request, *args, **kwargs):
        driver = Driver.objects.all()
        serializer = DriverLocation(driver, many=True)
        return Response(serializer.data)
