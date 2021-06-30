import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs

def main():
    # load()
    specials()
    exit()

def load():
    url = 'https://store.steampowered.com/'

    r = requests.get(url)

    soup = bs(r.content, 'html.parser')
    titles = soup.find_all("div", "home_title")
    categories = []
    for title in titles:
        categories.append(title.text.strip())
    print(categories)
    return None

def specials():
    url = 'https://store.steampowered.com/search/'
    payload = {
        'filter' : 'topsellers',
        'specials' : 1
    }
    r = requests.get(url, params=payload)
    print(r)
    soup = bs(r.content, 'html.parser')
    titles = []
    titles_raw = []
    titles_raw = soup.find_all('span','title')
    for title in titles_raw:
        titles.append(title.text.strip())
    print(titles)
    return None
main()