# Theo Rowlett
# Lab 14 - Dad Joke API

import requests
import json
import pprint

def main():
    # v1()      #Returns a random joke
    while True:
        v2()        #Returns a list of jokes based on a search
        val = input('Do you want to search for another joke (y/n)? ').lower()
        if val.lower() == 'n':
            break
    exit()

def v1():
    jokes = import_json_v1()
    print(jokes['joke'])
    return None

def v2():
    search_term = input("What joke do you want to search for? ")
    jokes = import_json_v2(search_term)
    for i in range(len(jokes['results'])):
        print(jokes['results'][i]['joke'] + '\n')
    return None

def import_json_v1():
    url = 'https://icanhazdadjoke.com/'
    header = {'accept': 'application/json'}
    raw = requests.get(url,headers = header)
    data = json.loads(raw.text)
    return data

def import_json_v2(search):
    url = 'https://icanhazdadjoke.com/search'
    header = {'accept': 'application/json'}
    payload = {'term':search}
    raw = requests.get(url,headers = header, params = payload)
    data = json.loads(raw.text)
    # pprint.pprint(data,indent=2)
    return data

main()