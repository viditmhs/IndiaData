'''
    Author: Vidit Maheshwrai
    Date: 20170602 (YYYYMMDD)
    Copyright :

    Purpose: gather data from Db

    History:

    Help: http://docs.mongoengine.org/tutorial.html

'''

# dependencies

import json

from mongoengine import *

import models as Model

EMPTY_REQUEST = "empty_request"
INVALID_REQUEST = "invalid_request"

def getAllStates():
    try:
        print("[INFO] Connecting DB")
        dbConnection = connect('indiaData')
        print("[INFO] Connection stablished")
        print(dbConnection)
        states = Model.State.objects;
        output = "{"
        comma = ""
        for s in states:
            output = output + comma;
            output = output + "\"" +s.state + "\"";
            comma = ","
        output = output + "}"
        return output;

    except Exception as e:
        error_message = "Error in Indian States"
        print (error_message, "Error Message", e)
        return error_message


def setState(data):
    state = Model.State
    jObject = json.loads(data)
    try:
        state = Model.State()
        state.state = jObject['state']
        state.cities = []
        print("[INFO] Connecting DB")
        dbConnection = connect('indiaData')
        print("[INFO] Connection stablished")
        #Checking is state already exist
        resp = getStateByName(jObject['state'])
        if(resp != None or resp == INVALID_REQUEST or resp== EMPTY_REQUEST):
            print(resp)
            return "{\"errorMessage\":\"State Invalid or State Exist\"}"
        else:
            state.save()
        return "{\"message\":\"Success\"}"


    except Exception as e:
        error_message = "Error In Saving Indian State " + data
        print (error_message, "Error Message", e)
        return error_message


def getStateByName(state):
    resp = ""
    try:
        if state == "":
            return EMPTY_REQUEST
        else:
            resp = Model.State.objects(Q(state=state));
            if(len(resp)<1):
                return None

    except json.JSONDecoder as e:
        print(e)
        resp = INVALID_REQUEST

    return resp

def setCities(data):
    state = Model.State
    jObject = json.loads(data)
    msg = ""
    try:
        # Get State
        # Check If Citi exist
        # If not then add else error

        dbConnection = connect('indiaData')

        #Checking is state already exist
        state = getStateByName(jObject['state'])
        if(state == None or state == INVALID_REQUEST or state== EMPTY_REQUEST):
            return "{\"errorMessage\":\"State Invalid\"}"
        else:
            cities = state[0].cities
            cityToAdd = jObject['cities']
            comma = ""
            for city in cityToAdd:
                if(city not in cities):
                    state.update(add_to_set__cities=city)
                    msg = msg + comma
                    comma = ","
                    msg = msg + "\"" + city + "\""
        return "{\"message\":\"Success\", \"citiesAdded\":[" + msg+"]}"


    except Exception as e:
        error_message = "Error In Saving Indian Cities " + data
        print (error_message, "Error Message", e)
        return error_message


def getAllCities(data):

    jObject = json.loads(data)
    try:
        dbConnection = connect('indiaData')

        # Checking is state already exist
        state = jObject['state']
        stateData = getStateByName(state)
        comma = ""
        citiesData = "{\""+ state+"\":"
        for city in stateData[0].cities:
            citiesData = citiesData + comma + "\"" + city + "\""
            comma = ","
        citiesData = citiesData + "}"

        return citiesData

    except Exception as e:
        error_message = "Error getting cities for request " + data
        print (error_message, "Error Message", e)
        return error_message