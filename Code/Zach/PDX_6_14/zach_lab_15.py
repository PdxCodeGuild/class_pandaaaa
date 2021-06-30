#Zach Watts
#Lab 15:  Quotes API

import requests
import json
import os 
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


def main():
    user_display()
    exit()

#-----------------------------VERSION 1------------------------------#
# def get_quotes(term=None,limit=20, page=1):
#     endpoint = 'https://favqs.com/api/qotd'
#     headers = {'Authorization': 'application/json'}
#     response = requests.get(endpoint, headers).json()
#     print(response['quote']['body'])
#     exit()

#-----------------------------VERSION 2------------------------------#

def get_quotes():
    keyword = keyword_search()
    endpoint = f'https://favqs.com/api/quotes?page=<page>&filter=<{keyword}>'
    load_dotenv()
    HEY = os.getenv('HELLO')
    headers1 = {'token': HEY}
    headers = {f'Authorization: Token token="{headers1["token"]}"': 'application/json'}
    response = requests.get(endpoint, headers)
    print(response)
    return 0

def keyword_search():
    keyword = input("Enter a keyword to search for related quotes or 'done' to exit:  ")
    return keyword

def user_display():
    get_quotes()
    valid = 0
    go_to_next = 0
    while not valid:
        next_page = input("Enter 'next page' or 'done':  ")
        if next_page == 'done':
            valid = 1
        elif next_page == 'next page':
            go_to_next = 1
            #go to next page
        else: print("Please enter a valid response")
    return 0


main()