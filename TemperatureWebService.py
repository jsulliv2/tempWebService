'''
    Filename:
        TemperatureWebService.p

    Description:
        Web service that takes temp input and returns JSON object containing converted temperature in other temperature units.
'''
from flask import Flask
import json

app = Flask(__name__)

returnTemp = {"fahrenheit": '', "celsius": '', "kelvin": '', "rankine": ''}


@app.route('/convert/fahrenheit/<fahr>/')
def fahrenheit(fahr):
    try:
        fahr = float(fahr)
    except ValueError:
        return("please be sure to enter a number and try again")
    returnTemp['celsius'] = (fahr-32)/1.8
    returnTemp['kelvin'] = (fahr + 459.67)*5/9
    returnTemp['rankine'] = fahr + 459.67
    del returnTemp['fahrenheit']
    return json.JSONEncoder().encode(returnTemp)


@app.route('/convert/celsius/<cels>/')
def celsius(cels):
    try:
        cels = float(cels)
    except ValueError:
        return("please be sure to enter a number and try again")
    returnTemp['fahrenheit'] = cels*9/5+32
    returnTemp['kelvin'] = cels+273.15
    returnTemp['rankine'] = (cels+273.15)*9/5
    del returnTemp['celsius']
    return json.JSONEncoder().encode(returnTemp)


@app.route('/convert/kelvin/<k>/')
def kelvin(k):
    try:
        k = float(k)
    except ValueError:
        return("please be sure to enter a number and try again")
    returnTemp['fahrenheit'] = k*9/5-459.67
    returnTemp['celsius'] = k-273.15
    returnTemp['rankine'] = k*9/5
    del returnTemp['kelvin']
    return json.JSONEncoder().encode(returnTemp)


@app.route('/convert/rankine/<ran>/')
def rankine(ran):
    try:
        ran = float(ran)
    except ValueError:
        return("please be sure to enter a number and try again")
    returnTemp['fahrenheit'] = ran-459.67
    returnTemp['celsius'] = (ran - 491.67)*5/9
    returnTemp['kelvin'] = ran*5/9
    del returnTemp['rankine']
    return json.JSONEncoder().encode(returnTemp)