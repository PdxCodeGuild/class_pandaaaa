# Theo Rowlett
# Lab 15
import requests
import json
import os
from dotenv import load_dotenv
from pprint import pprint

def main():
    r_quote = random_quote()
    print(r_quote['body'])
    print(f"- {r_quote['author']}")
    k_word = input("Enter the keyword you would like to search for: ")
    keyword(k_word)

    exit()

def random_quote():
    url ='https://favqs.com/api/qotd'
    r = requests.get(url)
    qotd = json.loads(r.text)
    # pprint(qotd)
    qotd = qotd['quote']
    return qotd

def keyword(k_word):
    url = 'https://favqs.com/api/quotes'
    load_dotenv()
    QUOTE_TOKEN = os.getenv('QUOTE_TOKEN')
    token = {
        'Authorization': 'Token token="' + QUOTE_TOKEN + '"'
    }
    payload = {
        'page' : 1,
        'filter' : k_word
    }

    while True:
        r = requests.get(url, headers=token, params=payload)
        print(r.url)
        data = json.loads(r.text)
        # pprint(data, indent=2)
        count = len(data['quotes'])
        print(f'{count} quotes associated with {k_word} on page {data["page"]}')
        if str(data['last_page']) == 'False':
            val = input('Enter "next" or "done" to go to next page: ').lower()
            if val == 'next':
                payload['page'] += 1
                continue
            elif val == 'done':
                break
            else:
                continue
        else:
            print('Last page')
            break
    return None

main()