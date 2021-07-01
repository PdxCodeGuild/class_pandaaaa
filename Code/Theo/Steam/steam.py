import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import json
import os
# from epicstore_api import EpicGamesStoreAPI as Epic

class Wishlist:
    def __init__(self,w_list) :
        self.w_list = w_list
        self.key_list = list(w_list.keys())
        self.length = len(self.key_list)
        self.games = []
        for i in range(self.length):
            title = w_list[self.key_list[i]]['name']
            try:
                steam_price  = float(w_list[self.key_list[i]]['subs'][0]['price'])/100
            except IndexError:
                steam_price = None
            new_game = Game(title,steam_price)
            self.games.append(new_game)
    def __str__(self):
        output = ''
        for i in range(self.length):
            output += str(self.games[i]) + '\n'
        return output
        
class Game:
    def __init__(self,title='',steam_price=''):
        self.title = title
        self.itad_title = title.lower().replace(' ','').replace(':','').replace('1','i').replace('2','ii').replace('3','iii').replace('4','IV')
        self.steam_price = steam_price
        self.epic_price = None
        self.gog_price = None
    def __str__(self) -> str:
        output = ''
        output += self.title
        output += '\n'
        output += f'Steam: {self.steam_price} Epic: {self.epic_price} GOG: {self.gog_price}'
        return output
    def __repr__(self) -> str:
        return f'{self.title} {self.steam_price}'
    
    def epic(self,e_price):
        self.epic_price = e_price
    def gog(self,gog_price):
        self.gog_price = gog_price

def main():
    warning()
    username = input("Enter username to retrieve wishlist: ")
    steamID = get_steamid(username)
    wishlist_games = get_wishlist(steamID)
    wishlist = Wishlist(wishlist_games)
    wishlist = itad(wishlist)
    print(wishlist)
    exit()

def get_steamid(username='OliveOil4Lube'):
    load_dotenv()
    STEAM_KEY = os.getenv('STEAM_KEY')
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
    r = requests.get(url)
    g = json.loads(r.text)
    return g

def itad(wishlist):
    url = 'https://api.isthereanydeal.com/v01/game/prices/'
    load_dotenv()
    ITAD_KEY = os.getenv('ITAD_KEY')
    for i in range(wishlist.length):
        # print(wishlist.games[i].itad_title)
        payload = {
            'key' : ITAD_KEY,
            'plains' : str(wishlist.games[i].itad_title),
            'country' : 'USA',
            'shops' : 'epic,gog'
        }
        r = requests.get(url,params=payload)
        game =json.loads(r.text)
        length = len(game['data'][wishlist.games[i].itad_title]['list'])
        if length != 0:
            for j in range(length):
                shop_id = game['data'][wishlist.games[i].itad_title]['list'][j]['shop']['id']
                price = game['data'][wishlist.games[i].itad_title]['list'][j]['price_new']
                if shop_id == 'epic':
                    wishlist.games[i].epic(price)
                if shop_id == 'gog':
                    wishlist.games[i].gog(price)
    return wishlist
        
def warning():
    print('Custom URL must be set under edit profile to work.')
main()