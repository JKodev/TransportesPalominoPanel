"""Transportes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

import main
from main.forms import LoginForm
from main.views import dashboard, WorkerList, WorkerCreate, WorkerUpdate, WorkerDelete, VehicleList, VehicleCreate, \
    VehicleUpdate, VehicleDelete, TravelList, TravelCreate, TravelUpdate, TravelDelete

urlpatterns = [
    url(r'^$', dashboard, name='init_dashboard'),
    url(r'^admin/', admin.site.urls),

    # Main URLs
    url(r'^dashboard/$', dashboard, name='main_dashboard'),

    # Worker URLs
    url(r'^worker/$', WorkerList.as_view(), name='main_worker_list'),
    url(r'^worker/create/$', WorkerCreate.as_view(), name='main_worker_create'),
    url(r'^worker/update/(?P<pk>[\w-]+)$', WorkerUpdate.as_view(), name='main_worker_update'),
    url(r'^worker/delete/(?P<pk>[\w-]+)$', WorkerDelete.as_view(), name='main_worker_delete'),

    # Vehicle URLs
    url(r'^vehicle/$', VehicleList.as_view(), name='main_vehicle_list'),
    url(r'^vehicle/create/$', VehicleCreate.as_view(), name='main_vehicle_create'),
    url(r'^vehicle/update/(?P<pk>[\w-]+)$', VehicleUpdate.as_view(), name='main_vehicle_update'),
    url(r'^vehicle/delete/(?P<pk>[\w-]+)$', VehicleDelete.as_view(), name='main_vehicle_delete'),

    # Travel URLs
    url(r'^travel/$', TravelList.as_view(), name='main_travel_list'),
    url(r'^travel/create/$', TravelCreate.as_view(), name='main_travel_create'),
    url(r'^travel/update/(?P<pk>[\w-]+)$', TravelUpdate.as_view(), name='main_travel_update'),
    url(r'^travel/delete/(?P<pk>[\w-]+)$', TravelDelete.as_view(), name='main_travel_delete'),

    url(r'^login/$', auth_views.login, {'template_name': 'main/login/login.html'}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
]
