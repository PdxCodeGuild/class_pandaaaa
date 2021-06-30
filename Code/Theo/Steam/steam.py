import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import json
import os


def main():
    warning()
    # username = input("Enter username to retrieve wishlist: ")
    # steamID = get_steamid(username)
    wishlist_games = get_wishlist()
    epic_scraper(wishlist_games['title'])
    # for i in range(len(wishlist_games['title'])):
    #    if (wishlist_games['steam'][i] != 'coming soon'): 
    #         print(wishlist_games['title'][i] + '\n'
    #         + 'Steam: $' + str(wishlist_games['steam'][i]) + '\n')
    #         + 'EGS: $' + wishlist_games['epic'][i])
    exit()

def get_steamid(username='OliveOil4Lube'):
    load_dotenv()
    STEAM_KEY = os.getenv('STEAM_KEY')
    # print(STEAM_KEY)
    url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'
    payload = {
        'key' : STEAM_KEY,
        'vanityurl' : username
    }
    r = requests.get(url,params=payload)
    user = json.loads(r.text)
    return user['response']['steamid']

def get_wishlist(steamID='76561198918721504'):
    url = 'https://store.steampowered.com/wishlist/profiles/' + steamID + '/wishlistdata/'
    games = {
        'title' : [],
        'steam' : [],
        'epic' : []
    }
    r = requests.get(url)
    g = json.loads(r.text)
    keys = list(g.keys())
    for i in range(len(g)):
        games['title'].append(g[keys[i]]['name'])
        try:
            games['steam'].append(float(g[keys[i]]['subs'][0]['price'])/100)
            # pprint(g[keys[i]]['subs'][0]['price'],indent=1)
        except IndexError:
            games['steam'].append("coming soon")
    return games

def epic_scraper(games):
    epic_prices = []
    url = 'https://www.epicgames.com/store/en-US/p/'
    print(games[9].lower().replace(" ","-"))
    r = requests.get(url + games[9].lower().replace(" ","-"))
    # print(r)
    # pprint(r.url)
    soup = bs(r.text,'html.parser')
    # print(soup.text)
    # output for game not found will be a diff url : 'https://www.epicgames.com/store/en-US/not-found'

def warning():
    print('Custom URL must be set under edit profile to work.')
main()