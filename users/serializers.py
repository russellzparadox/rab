from rest_framework import serializers

from users.models import Driver


class DriverLocation(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['l_x', 'l_y']
        # , 'city', 'establishedYear', 'NumberOfFaculties'
