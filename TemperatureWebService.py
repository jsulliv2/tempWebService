'''
    Filename:
        TemperatureWebService.py

    Description:
        Web service that takes temp input and returns JSON object containing converted temperature in other temperature units.
'''
from flask import Flask
from json import JSONEncoder

app = Flask(__name__)


def fahrenheit(fahr):
    returnTemp = {}
    returnTemp['celsius'] = (fahr-32)/1.8
    returnTemp['kelvin'] = (fahr + 459.67)*5/9
    returnTemp['rankine'] = fahr + 459.67
    return returnTemp


def celsius(cels):
    returnTemp = {}
    returnTemp['fahrenheit'] = cels*9/5+32
    returnTemp['kelvin'] = cels+273.15
    returnTemp['rankine'] = (cels+273.15)*9/5
    return returnTemp


def kelvin(k):
    returnTemp = {}
    returnTemp['fahrenheit'] = k*9/5-459.67
    returnTemp['celsius'] = k-273.15
    returnTemp['rankine'] = k*9/5
    return returnTemp


def rankine(ran):
    returnTemp = {}
    returnTemp['fahrenheit'] = ran-459.67
    returnTemp['celsius'] = (ran - 491.67)*5/9
    returnTemp['kelvin'] = ran*5/9
    return returnTemp


@app.route('/convert/<unit>/<temp>/')
def main(unit, temp):
    results = {}
    unit = unit.lower()
    absoluteZero = {'kelvin': 0, 'rankine': 0, 'celsius': -273.15, 'fahrenheit': -459.67}
    try:
        temp = float(temp.replace(",", "").replace(" ", ""))
    except Exception as e:
        raise e('Error turning temp input into a number')
    if temp < absoluteZero[unit]:
        raise Exception('Value provided is below absoluteZero')
    if unit == 'fahrenheit':
        results = fahrenheit(temp)
    elif unit == 'celsius':
        results = celsius(temp)
    elif unit == 'rankine':
        results = rankine(temp)
    elif unit == 'kelvin':
        results = kelvin(temp)
    if results.keys():
        return JSONEncoder().encode(results)
