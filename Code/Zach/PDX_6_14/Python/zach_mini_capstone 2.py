#Zach Watts
#Mini Capstone: How close am I to where the Zodiac Killer Struck?

import googlemaps
import math
import os 
from dotenv import load_dotenv

strikes = [{
    "Victim(s)" : "David Arthur Faraday, 17, and Betty Lou Jensen, 16",
    "lat" : 38.094892, 
    "long" : -122.143956,
    "Description" : "CONFIRMED STRIKE: On December 20, 1968, \
David Arthur Faraday, 17, and Betty Lou Jensen, 16 were shot \
and killed, on Lake Herman Road, within the city limits of Benicia."
}, {
    "Victim(s)" : "Michael Renault Mageau, 19, and Darlene Elizabeth Ferrin, 22",
    "lat" : 38.125989,
    "long" :  -122.191094,
    "Description" : "CONFIRMED STRIKE: On July 4, 1969, Michael \
Renault Mageau, 19, and Darlene Elizabeth Ferrin, 22 were shot \
in the parking lot of Blue Rock Springs Park in Vallejo. While \
Mageau survived the attack, Ferrin was pronounced dead on arrival \
at Kaiser Foundation Hospital."
}, {
    "Victim(s)" : "Bryan Calvin Hartnell, 20, and Cecelia Ann Shepard, 22",
    "lat" : 38.563414, 
    "long" : -122.231786,
    "Description" : "CONFIRMED STRIKE: On September 27, 1969, Bryan Calvin \
Hartnell, 20, and Cecelia Ann Shepard, 22 were stabbed at Lake Berryessa \
in Napa County. Hartnell survived eight stab wounds to the back, but Shepard \
died as a result of her injuries on September 29, 1969. "
}, {
    "Victim(s)" : "Paul Lee Stine, 29",
    "lat" : 37.788742, 
    "long" : -122.457094,
    "Description" : "CONFIRMED STRIKE: On October 11, 1969, Paul Lee Stine, 29\
was shot and killed  in the Presidio Heights neighborhood in San Francisco. "
}, {
    "Victim(s)" : "Robert Domingos, 18, and Linda Edwards, 17",
    "lat" : 34.469778, 
    "long" : -120.16865,
    "Description" : "SUSPECTED STRIKE: On June 4, 1963, Robert Domingos, 18, \
and Linda Edwards, 17, were shot and killed  on a beach near Gaviota. \
Edwards and Domingos were identified as possible Zodiac victims because \
of specific similarities between their attack and the Zodiac's attack at \
Lake Berryessa six years later."
}, {
    "Victim(s)" : "Cheri Jo Bates, 18",
    "lat" : 33.971944,
    "long" : -117.381111,
    "Description" : "SUSPECTED STRIKE:  On October 30, 1966, Cheri Jo Bates, 18, \
was stabbed to death and nearly decapitated at Riverside City College in \
Riverside. Bates's possible connection to the Zodiac only appeared four years \
after her murder when San Francisco Chronicle reporter Paul Avery received a \
tip regarding similarities between the Zodiac killings and the circumstances \
surrounding Bates's death.",
}, {
    "Victim(s)" : "Donna Lass, 25",
    "lat" : 39.061002145317744,
    "long" : -120.014764840426,
    "Description" : "SUSPECTED STRIKE:  Donna Lass, 25, was last seen \
September 6, 1970, in Stateline, Nevada. A postcard with an \
advertisement from Forest Pines condominiums (near Incline Village \
at Lake Tahoe) pasted on the back was received at the Chronicle on March \
22, 1971, and has been interpreted as the Zodiac claiming Lass's \
disappearance as a victim. No evidence has been uncovered to connect \
Lass's disappearance with the Zodiac Killer definitively,"
}, {
    "Victim(s)" : "Kathleen Johns, 22",
    "lat" : 37.637817,
    "long" : -121.398672,
    "Description" : "SUSPECTED STRIKE (ESCAPED): Kathleen Johns, 22 was \
allegedly abducted on March 22, 1970, on Highway 132 near I-580, in an \
area west of Modesto. Johns escaped from the car of a man who drove her \
and her infant daughter around the area between Stockton and Patterson \
for approximately 1½ hours."
}]


def main():
    address = get_address()
    lat, long = get_coordinates(address)
    nearest_strk = calc_strike_dist(lat, long)
    strike_report(nearest_strk, lat, long)
    exit()

def get_coordinates(address):
    load_dotenv()
    key = os.getenv('KEY')
    gmaps = googlemaps.Client(key)
    geocode_result = gmaps.geocode(address)
    coords = geocode_result[0]['geometry']['location']
    lat = coords['lat']
    long = coords['lng']
    return lat, long

def get_address():
    street = input("Enter your street and building number:  ")
    city = input("Enter your city:  ")
    state = input("Enter your state in two capital letter format:  ")
    address = f'{street}, {city}, {state}'
    return address

def calc_dist(lat_user, long_user, lat_strike, long_strike):
    # Haversine Formala from kite.com
    R = 6373.0
    lat1 = math.radians(lat_user)
    lon1 = math.radians(long_user)
    lat2 = math.radians(lat_strike)
    lon2 = math.radians(long_strike)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def calc_strike_dist(lat_, long_):
    strike_lst = []
    for strike in strikes:
        strike_lst.append(round(calc_dist(lat_, long_, strike["lat"], strike["long"]), 2))
    strike_lst.sort()
    nearest_strk = strike_lst[0]
    return nearest_strk

def strike_report(nearest_strk_, lat_, long_):
    strk_rpt = ""
    for strike in strikes:
        if nearest_strk_ == round(calc_dist(lat_, long_, strike['lat'], strike['long']), 2):
            strk_rpt = strike["Description"]
    print(strk_rpt)
    print(f'\nThis strike took place {round(nearest_strk_*0.621371, 0)} miles from your location. \n\
    \nAlthough the Zodiac claimed 37 murders in letters to the newspapers, \n\
investigators agree on only seven confirmed victims, two of whom survived.\n')
    return strk_rpt


main()