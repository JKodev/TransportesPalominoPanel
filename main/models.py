
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class City(models.Model):
    name = models.CharField("Ciudad", max_length=200, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


class Charge(models.Model):
    name = models.CharField("Cargo", max_length=120, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cargo"


class LicenseType(models.Model):
    name = models.CharField("Tipo", max_length=60, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo de Licencia"


class Person(User):
    birthday = models.DateField("Cumpleaños", blank=False)
    document = models.CharField("DNI", max_length=8, null=False, blank=False)
    charge = models.ForeignKey(Charge, related_name="Person_Charge")
    license_type = models.ForeignKey(LicenseType, related_name="Person_LicenseType")
    license = models.CharField("Brevete", blank=False, max_length=30)
    telephone = models.CharField("Telefono", blank=True, null=True, max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.document
        super(Person, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Trabajador"


class Vehicle(models.Model):
    plaque = models.CharField("Placa", max_length=8,  blank=False, null=False)
    model = models.CharField("Modelo", max_length=22, blank=False, null=False)
    mark = models.CharField("Marca", max_length=32, blank=False, null=False)
    year = models.IntegerField("Año", blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vehículo"


class Travel(models.Model):
    origin = models.ForeignKey(City, related_name='origin_city', null=True)
    destination = models.ForeignKey(City, related_name='destination_city', null=True)
    driver = models.ForeignKey(Person, related_name="Travel_Driver")
    vehicle = models.ForeignKey(Vehicle, related_name="Travel_Vehicle")
    departure_date = models.DateTimeField("Fecha de Salida", blank=False, null=False)
    arrival_date = models.DateTimeField("Fecha de Llegada", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Viaje"


class Incidents(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    latitude = models.CharField("Latitud", max_length=20, blank=False, null=True)
    longitude = models.CharField("Longitud", max_length=20, blank=False, null=True)
    message = models.CharField("Mensaje", max_length=200, blank=False, null=True)
    driver = models.ForeignKey(Person, related_name='incident_person', null=True)
    vehicle = models.ForeignKey(Vehicle, related_name='incident_vehicle', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
