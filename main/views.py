from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from main.forms import PersonForm, VehicleForm, TravelForm
from main.models import Person, Charge, Vehicle, Travel, Incidents


@login_required(login_url='/login/')
def dashboard(request):
    title = 'Bienvenidos'
    return render(request, 'main/index.html', locals())


class WorkerList(ListView):
    queryset = Person.objects.filter(is_active=True)
    template_name = 'main/worker/index.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerList, self).dispatch(request, *args, **kwargs)


class WorkerCreate(CreateView):
    template_name = 'main/worker/create.html'
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('main_worker_list')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerCreate, self).dispatch(request, *args, **kwargs)


class WorkerUpdate(UpdateView):
    template_name = 'main/worker/create.html'
    model = Person
    form_class = PersonForm
    success_url = '/worker'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerUpdate, self).dispatch(request, *args, **kwargs)


class WorkerDelete(DeleteView):
    template_name = 'main/worker/delete.html'
    model = Person
    success_url = reverse_lazy('main_worker_list')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerDelete, self).dispatch(request, *args, **kwargs)


class VehicleList(ListView):
    model = Vehicle
    template_name = 'main/vehicles/index.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(VehicleList, self).dispatch(request, *args, **kwargs)


class VehicleCreate(CreateView):
    template_name = 'main/vehicles/create.html'
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('main_vehicle_list')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(VehicleCreate, self).dispatch(request, *args, **kwargs)


class VehicleUpdate(UpdateView):
    template_name = 'main/vehicles/create.html'
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('main_vehicle_list')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(VehicleUpdate, self).dispatch(request,*args, **kwargs)


class VehicleDelete(DeleteView):
    template_name = 'main/vehicles/delete.html'
    model = Vehicle
    success_url = reverse_lazy('main_vehicle_list')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(VehicleDelete, self).dispatch(request,*args, **kwargs)


class TravelList(ListView):
    model = Travel
    template_name = 'main/travel/index.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(TravelList, self).dispatch(request, *args, **kwargs)


class TravelCreate(CreateView):
    template_name = 'main/travel/create.html'
    model = Travel
    form_class = TravelForm
    success_url = reverse_lazy('main_travel_list')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(TravelCreate, self).dispatch(request, *args, **kwargs)


class TravelUpdate(UpdateView):
    template_name = 'main/travel/create.html'
    model = Travel
    form_class = TravelForm
    success_url = reverse_lazy('main_travel_list')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(TravelUpdate, self).dispatch(request, *args, **kwargs)


class TravelDelete(DeleteView):
    template_name = 'main/travel/delete.html'
    model = Travel
    success_url = reverse_lazy('main_travel_list')

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(TravelDelete, self).dispatch(request, *args, **kwargs)


def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('main_dashboard'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('main_dashboard'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        mensaje = 'Nombre de usuario o contrasena no valido'
    return render(request, 'main/login/login.html', {'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return redirect('/login/')


class IncidentsList(ListView):
    model = Incidents
    template_name = 'main/incident/index.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(IncidentsList, self).dispatch(request, *args, **kwargs)
