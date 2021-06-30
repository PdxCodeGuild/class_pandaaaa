# https://openweathermap.org/api/one-call-api#data - Weather data API
# https://geocode.xyz/api
# Theo Rowlett

import requests
import json
import os
from dotenv import load_dotenv
from pprint import pprint

def main():
    load_dotenv()
    address = input("Input the address that you would like to find the weather for: ")
    locate = location(address)
    latt = locate['latt']
    longt = locate['longt']
    weather_now(latt,longt)
    # pprint(locate, indent=2)

    exit()

def location(address):
    GEOCODE_XYZ = os.getenv('GEOCODE_XYZ')
    url = 'https://geocode.xyz/'
    payload = {
        'auth': GEOCODE_XYZ,
        'locate' : address,
        'region' : 'USA',
        'json' : 1
    }
    r = requests.get(url, params = payload)
    return json.loads(r.text)

def weather_now(latt=45.66138,longt=-122.58383):
    WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')
    url = 'https://api.openweathermap.org/data/2.5/onecall'

    payload = {
        'lat':str(latt),
        'lon':str(longt),
        'dt':'',
        'appid' : WEATHER_TOKEN,
        'units' : 'imperial'
    }

    r = requests.get(url, params=payload)
    print(r.url)
    print(r)
    data = json.loads(r.text)
    pprint(data['current'],indent=2)
    return None

main()