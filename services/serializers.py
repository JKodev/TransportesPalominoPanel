from rest_framework import serializers

from main.models import Incidents, Person, LicenseType, Vehicle


class LicenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseType
        fields = ['name', ]


class PersonSerializer(serializers.ModelSerializer):
    license_type = LicenseTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthday', 'document', 'charge', 'license_type', 'license', 'telephone', ]


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['plaque', 'model', 'mark', 'year', ]


class IncidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = ['when', 'latitude', 'longitude', 'message', 'driver', 'vehicle', ]
