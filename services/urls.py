from django.conf.urls import url

from services import views

urlpatterns = [
    url(r'^incidents/$', views.IncidentsList.as_view(), name='service-incidents'),
    url(r'^incidents/test/$', views.IncidentsListTest.as_view(), name='service-incidents-test'),
]