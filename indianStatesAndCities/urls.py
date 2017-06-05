'''
    Name: Vidit Maheshwari
    Description:
'''

from django.conf.urls import url

from . import services

urlpatterns = [
    url(r'^addState', services.addState, name='addState'),
    url(r'^addCities', services.addCities, name='addCities'),
    url(r'^getStates', services.getStates, name='getStates'),
    url(r'^getCities', services.getCities, name='getCities'),
]