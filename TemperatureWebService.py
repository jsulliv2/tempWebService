'''
    Filename:
        TemperatureWebService.py

    Description:
        Web service that takes temp input and returns JSON object containing converted temperature in other temperature units.
'''
from flask import Flask
from json import JSONEncoder
import sys

app = Flask(__name__)

#take kelvin temp and create dict containing values for all temps
def kelvin(k):
    returnTemp = {}
    returnTemp['kelvin'] = k
    returnTemp['fahrenheit'] = k*9/5-459.67
    returnTemp['celsius'] = k-273.15
    returnTemp['rankine'] = k*9/5
    return returnTemp

#turn temp into kelvin, check for absolute zero
def translate(unit, temp):
    toKelv = {'fahrenheit': (temp+459.67)*5/9, 'celsius': temp+273.15, 'rankine': temp*5/9, 'kelvin': temp}
    temp = toKelv[unit]
    if temp < 0:
        raise Exception('Entered number is below absolute zero')
    return temp

@app.route('/convert/<unit>/<temp>/')
def main(unit, temp):
    unit = unit.lower()
    if unit not in ('kelvin', 'celsius', 'rankine', 'fahrenheit'):
        raise Exception('Unsupported unit entered, please use kelvin, fahrenheit, celsius, or rankine.')
    results = {}
    try:
        temp = float(temp.replace(",", "").replace(" ", ""))
    except Exception as e:
        raise e('Error turning temp input into a number')
    temp = translate(unit, temp)
    results = kelvin(temp)
    results.pop(unit)
    if results:
        return JSONEncoder().encode(results)
    else:
        raise Exception("Return object empty.")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        debug = sys.argv[1]
    elif len(sys.argv) > 2:
        print('Usage is: python3 TemperatureWebService.py True/False. \n True/False is whether to engage the flask debugger')
        sys.exit()
    else:
        debug = ''
    app.run(debug=debug)
    