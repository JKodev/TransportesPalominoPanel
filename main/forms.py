from datetime import date

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from Transportes import settings
from main.models import Charge, LicenseType, Person, Vehicle, Travel, City


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class ChargeModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class LicenseTypeModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class PersonModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name + " " + obj.last_name


class VehicleModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.plaque


class CityModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class ChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = ['name', ]


class LicenseTypeForm(forms.ModelForm):
    class Meta:
        model = LicenseType
        fields = ['name', ]


class PersonForm(forms.ModelForm):
    birthday = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    charge = ChargeModelChoiceField(queryset=Charge.objects.all())
    license_type = LicenseTypeModelChoiceField(queryset=LicenseType.objects.all())

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombres'
        self.fields['first_name'].widget.attrs['required'] = 'true'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellidos'
        self.fields['last_name'].widget.attrs['required'] = 'true'
        self.fields['birthday'].widget.attrs['class'] += ' datepicker'

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthday', 'document', 'charge', 'license_type', 'license', 'telephone', ]


class VehicleForm(forms.ModelForm):
    year = forms.IntegerField(max_value=date.today().year)

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['year'].widget.attrs['max'] = date.today().year
        self.fields['year'].widget.attrs['min'] = int(date.today().year)-20

    def clean(self):
        cleaned = super(VehicleForm, self).clean()
        plaque = cleaned.get('plaque')
        if Vehicle.objects.filter(plaque=plaque).count() > 0:
            self.add_error('plaque', 'Esta placa ya se encuentra registrada')

    class Meta:
        model = Vehicle
        fields = ['plaque', 'model', 'mark', 'year', ]


class TravelForm(forms.ModelForm):
    origin = CityModelChoiceField(queryset=City.objects.all())
    destination = CityModelChoiceField(queryset=City.objects.all())
    driver = PersonModelChoiceField(queryset=Person.objects.filter(is_active=True, Travel_Driver__isnull=True))
    vehicle = VehicleModelChoiceField(queryset=Vehicle.objects.filter(Travel_Vehicle__isnull=True))

    def __init__(self, *args, **kwargs):
        super(TravelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Travel
        exclude = ['created_at', 'updated_at', ]
