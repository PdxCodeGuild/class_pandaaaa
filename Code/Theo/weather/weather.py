# https://openweathermap.org/api/one-call-api#data - Weather data API
# Theo Rowlett

import requests
import json
import os
from dotenv import load_dotenv
from pprint import pprint
# from geopy import geocoders
from geopy.geocoders import Nominatim

def main():
    load_dotenv()
    address = input("Input the address that you would like to find the weather for: ")
    location = geocode(address)
    lat = location.latitude
    longt = location.latitude
    data = weather(lat,longt)
    pprint(data['current'], indent=2)
    exit()

def geocode(address):
    geolocator = Nominatim(user_agent="Theo's weather app")
    location = geolocator.geocode(address)
    return location

def weather(lat=45.66138,longt=-122.58383):
    WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')
    url = 'https://api.openweathermap.org/data/2.5/onecall'

    payload = {
        'lat':str(lat),
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
    return data

if __name__=='__main__':
    main()