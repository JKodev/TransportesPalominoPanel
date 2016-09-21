from django.contrib import admin

from main.models import Person, Charge, LicenseType, Travel, Vehicle, City


@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', ]


@admin.register(LicenseType)
class LicenseTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    pass


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    exclude = ('password', 'last_login', 'groups', 'is_staff', 'is_active', 'date_joined', 'objects', 'is_superuser', 'user_permissions')
