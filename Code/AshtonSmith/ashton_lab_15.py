# Lab 15: Quotes API
# For this lab we'll be using the Favqs Quotes API to first get a random quote,
import requests
import json
import os
from dotenv import load_dotenv



#prog main
def main():
    request_quote_search(input("Enter a term to search for: "))
    return 0



#this function quests a quote
def request_quote():
    url = 'https://favqs.com/api/qotd'
    response = requests.get(url, headers = {'Accept' : 'application/json'})#send a get request
    # data = response.json()
    data = json.loads(response.text)
    print(data)



#search by term
def request_quote_search(term):
    url = f'https://favqs.com/api/quotes?page=1&filter={term}'
    last_page = False
    again = ''
    payload ={ 
        'page' : '1',
        'term' : f'{term}'
    }
    load_dotenv()
    token = os.getenv('TOKEN')
    headers = {'Authorization': 'Token token="' + str(token) + '"'}
    count = 1
    quote_count = 1
    while not(last_page) and again != 'x':
        response = requests.get(url, headers= headers, params= payload)
        data = response.json()
        for i in data['quotes']:
            print('Quote ' + str(quote_count) + '.')
            print (i['body'] + ' - ' + i['author'])
            print('\n\n')
            quote_count += 1
        last_page = data['last_page']
        print('Page: ' + str(count) + '.')
        again = input('Again? Enter x to exit or enter to continue to the next page.')
        payload['page'] = str(int(payload['page']) + 1)
        count += 1



main()