# https://openweathermap.org/api/one-call-api#data - Weather data API
# Theo Rowlett

import requests
import json
import os
from dotenv import load_dotenv
from pprint import pprint
from geopy.geocoders import Nominatim

def main():
    while True:
        address = input("Input the address that you would like to find the weather for: ")
        if address == '':
            continue
        location = geocode(address)
        # If the address is not valid, geocode will return a NoneType w/ value None
        if location!= None:
            lat = location.latitude
            longt = location.latitude
            data = weather(lat,longt)
            print(location)
            pprint(data['current'], indent=2)
            break
        else:
            print("Invalid location, try again")
    exit()

def geocode(address):
    geolocator = Nominatim(user_agent="Theo's weather app")
    location = geolocator.geocode(address)
    return location

def weather(lat=45.66138,longt=-122.58383):
    load_dotenv()
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
    data = json.loads(r.text)
    return data

if __name__=='__main__':
    main()