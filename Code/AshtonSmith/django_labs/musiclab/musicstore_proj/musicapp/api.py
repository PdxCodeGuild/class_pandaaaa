#this file will be used to handel data from the deezer api


from urllib.request import urlopen
import requests
import ast
import json
# url = https://api.deezer.com/version/service/id/method/?parameters
# GET /search/artist/?q=eminem&index=0&limit=2&output=xml


def main():
    my_data = request_data()
    return 0

def request_search(to_search):
    url = f'https://api.deezer.com/search?q={to_search}'
    response = requests.get(url)
    my_data = json.loads(response.content.decode('utf-8'))
    return my_data

def request_list(url):
    print('------------------------------------------------------')
    print(url)
    response = requests.get(url)

    my_data = json.loads(response.content.decode('utf-8'))
    return my_data['data']


def request_data():
    url = 'https://api.deezer.com/chart/0/tracks'
    response = requests.get(url)
    my_data = json.loads(response.content.decode('utf-8'))
    return my_data['data']

def request_artist(id):
    url = f'https://api.deezer.com/artist/{id}'
    response = requests.get(url)
    my_data = json.loads(response.content.decode('utf-8'))
    return my_data

def request_radio():
    url = f'https://api.deezer.com/radio/genres'
    response = requests.get(url)
    my_data = json.loads(response.content.decode('utf-8'))
    return my_data['data']



def request_radio_tracks(id):
    url = f"https://api.deezer.com/radio/{id}/tracks"
    response = requests.get(url)
    my_data = json.loads(response.content.decode('utf-8'))
    return my_data['data']

def request_song(id):
    url = f'https://api.deezer.com/track/{id}'
    response = requests.get(url)
    my_data = json.loads(response.content.decode('utf-8'))
    return my_data
# for item in my_data['data']:
#         print('-------------------item')
#         print(item['title'])

#         print('-------------------artist')
#         print(item['artist'])

#         print('-------------------album')
#         print(item['album'])
