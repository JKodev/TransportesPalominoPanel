from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from twilio.rest import TwilioRestClient

from Transportes import settings
from main.models import Incidents, Person, Vehicle
from services.serializers import IncidentsSerializer, PersonSerializer, VehicleSerializer


class IncidentsList(APIView):
    def get(self, request, format=None):
        incidents = Incidents.objects.all()
        serializer = IncidentsSerializer(incidents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = IncidentsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            driver = Person.objects.get(pk=data['driver'])
            fullname = driver.first_name + " " + driver.last_name
            last_ubication = data['latitude'] + ", " + data['longitude']
            sms = "El conductor " + fullname + ". Esta mostrando signos de suenio. Ubicacion: " + last_ubication
            client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID, token=settings.TWILIO_TOKEN)
            message = client.messages.create(body=sms,
                                             to=settings.TWILIO_PHONE_INSPECTOR,
                                             from_=settings.TWILIO_PHONE_NUMBER)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncidentsListTest(APIView):
    def get(self, request, format=None):
        incidents = Incidents.objects.all()
        serializer = IncidentsSerializer(incidents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = IncidentsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
