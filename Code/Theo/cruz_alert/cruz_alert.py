import requests
from dotenv import load_dotenv
import os
import json
from pprint import pprint

def main():
    BEARER_TOKEN = token()
    # print(BEARER_TOKEN)
    author_id = get_user_id(BEARER_TOKEN)
    tweet_id = get_recent_tweet(BEARER_TOKEN, author_id)
    exit()
    
def token():
    load_dotenv()
    return os.getenv('TWITTER_BEARER')

def get_user_id(BEARER_TOKEN):
    url = 'https://api.twitter.com/2/users/by'
    payload = {
        'usernames' : 'TedCruz'
    }
    r = requests.get(url,headers=return_header(BEARER_TOKEN),params=payload)
    data = json.loads(r.text)
    pprint(data,indent=2)
    id = data['data'][0]['id']
    return id

def return_header(BEARER_TOKEN):
    header = {
        'Authorization' : f'Bearer {BEARER_TOKEN}'
    }
    return header
    
def get_recent_tweet(BEARER_TOKEN,author_id):
    url = 'https://api.twitter.com/2/tweets/search/recent'
    payload = {
        'query' : 'from:tedcruz -is: retweet',
        # 'tweet.fields' : f'geo',
        'place_fields' : 'country_code'
    }
    r = requests.get(url,headers=return_header(BEARER_TOKEN),params=payload)
    print(r)
    data = json.loads(r.text)
    pprint(data, indent=2)
    return data['data'][0]['id']
    
if __name__ == "__main__":
    main()