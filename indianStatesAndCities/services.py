'''
    Name: Vidit Maheshwari

    Description:

    History:

'''
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import indianStatesAndCitiesDao
import Utility as util

@csrf_exempt
def getStates(request):
    print("[INFO] Request to get states received.")
    if request.method == 'GET':
        return HttpResponse("GET request not accepted")
    elif request.method == 'POST':
        try:
            print(request.META['HTTP_USER_AGENT'])
        except Exception as e:
            print("No User Agent")
        resp =indianStatesAndCitiesDao.getAllStates();
        return HttpResponse(resp)
    else:
        return HttpResponse("Invalid request")

@csrf_exempt
def getCities(request):
    print("[INFO] Request to get cities received.")
    if request.method == 'GET':
        return HttpResponse("GET request not accepted")
    elif request.method == 'POST':
        try:
            print(request.META['HTTP_USER_AGENT'])
        except Exception as e:
            print("No User Agent")
        resp =indianStatesAndCitiesDao.getAllCities(request.body);
        return HttpResponse(resp)
    else:
        return HttpResponse("Invalid request")

@csrf_exempt
def addState(request):
    print("[INFO] Request to add state received.")
    if request.method == 'GET':
        return HttpResponse("GET request not accepted")
    elif request.method == 'POST':
        if (util.authentication(request)):
            resp =indianStatesAndCitiesDao.setState(request.body);
            return HttpResponse(resp)
        else:
            return HttpResponse("Access Denied")
    else:
        return HttpResponse("Invalid request")

@csrf_exempt
def addCities(request):
    print("[INFO] Request to add cities received.")
    if request.method == 'GET':
        return HttpResponse("GET request not accepted")
    elif request.method == 'POST':
        if (util.authentication(request)):
            resp =indianStatesAndCitiesDao.setCities(request.body);
            return HttpResponse(resp)
        else:
            return HttpResponse("Access Denied")
    else:
        return HttpResponse("Invalid request")