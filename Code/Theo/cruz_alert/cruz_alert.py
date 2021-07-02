import requests
from dotenv import load_dotenv
import os
import json
from pprint import pprint
from american_cities import load_cities

def main():
    cities = load_cities()
    BEARER_TOKEN = token()
    author_id = get_author_id(BEARER_TOKEN)
    tweets = get_recent_tweets(BEARER_TOKEN)
    location = scrape_tweets(tweets,cities)
    if location == False:
        print('Ted Cruz is on the loose, stay vigilant.')
    else:
        print(f"He's in {location}. Stay safe.")
    exit()
    
def token():
    load_dotenv()
    return os.getenv('TWITTER_BEARER')

def get_author_id(BEARER_TOKEN,username='tedcruz'):
    url = 'https://api.twitter.com/2/users/by'
    payload = {
        'usernames' : username
    }
    r = requests.get(url,headers=return_header(BEARER_TOKEN),params=payload)
    data = json.loads(r.text)
    # pprint(data,indent=2)
    id = data['data'][0]['id']
    return id

def return_header(BEARER_TOKEN):
    header = {
        'Authorization' : f'Bearer {BEARER_TOKEN}'
    }
    return header
    
def get_recent_tweets(BEARER_TOKEN,username='tedcruz'):
    url = 'https://api.twitter.com/2/tweets/search/recent'
    payload = {
        'query' : f'from:{username} -is: retweet',
        # 'tweet.fields' : f'geo',
    }
    r = requests.get(url,headers=return_header(BEARER_TOKEN),params=payload)
    data = json.loads(r.text)
    # print(data['data'][0])
    return data['data']
    
def scrape_tweets(tweets,cities):
    #i is for tweet
    #j is for words within the tweet
    #k is to loop through the list of American city names
    print(tweets[0]['text'].split())
    
    for i in range(len(tweets)):
        tweet_words = tweets[i]['text'].split()
        for j in range(len(tweet_words)):
            for k in range(len(cities)):
                if j == cities[k].name:
                    print(cities[k].name)
                    return cities[k].name
    return False

if __name__ == "__main__":
    main()