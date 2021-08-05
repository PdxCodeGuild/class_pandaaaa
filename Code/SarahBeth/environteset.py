import os 
import requests
# from dotenv import load_dotenv

# load_dotenv()

# HEY = os.getenv('HELLO')

# print(HEY)

# headers = {'token': HEY}

# url = 'https://favqs.com/api/quotes/?filter=funny'
# token = 'd055d363712be70f2cd35ec5f360a528'
# headers = {'Authorization': 'Token token="d055d363712be70f2cd35ec5f360a528"'}
QUOTE_TOKEN = 'd055d363712be70f2cd35ec5f360a528'
url = 'https://favqs.com/api/quotes'
token = {
        'Authorization': 'Token token="' + QUOTE_TOKEN + '"'
    }
payload = {
        'page' : 1,
        'filter' : 'cat'
    }

r = requests.get(url, headers=token, params=payload)
print(r.url)