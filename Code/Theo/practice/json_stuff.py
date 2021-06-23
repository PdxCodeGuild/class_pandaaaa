import json
import requests

def main():
    url = ''
    payload = {
        'format':'json'
    }
    r = requests.get(url, params=payload)
    print(r.url)
    exit()
    
main()