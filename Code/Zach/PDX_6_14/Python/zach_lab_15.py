#Zach Watts
#Lab 15:  Quotes API

import requests
import json
import os 
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

def main():
    get_quotes()
    exit()

#-----------------------------VERSION 1------------------------------#
# def get_quotes():
#     endpoint = 'https://favqs.com/api/qotd'
#     headers = {'Authorization': 'application/json'}
#     response = requests.get(endpoint, headers).json()
#     print(response['quote']['body'])
#     exit()

#-----------------------------VERSION 2------------------------------#

def get_quotes():
    keyword = keyword_search()
    if keyword == 'done':
        exit()
    page = 1
    endpoint = f'https://favqs.com/api/quotes?page=<page>&filter=<{keyword}>'
    load_dotenv()
    key = os.getenv('QUOTE_KEY')
    headers = {'Authorization': f'Token token="{key}"'}
    params = {'page' : page}
    response = requests.get(endpoint, headers=headers, params=params)
    print(response.json()['quotes'][0]['body'])
    next_page = True
    while next_page == True: 
        page_forward = input("Enter 'next page' or 'done' to exit:  ")
        if page_forward == 'next page':
            next_page = True
            page = page + 1
            params = {'page' : page}
        else:
            next_page = False
        response = requests.get(endpoint, headers=headers, params=params)
        print(response.json()['quotes'][0]['body'])
    return 0

def keyword_search():
    keyword = input("Enter a keyword to search for related quotes or 'done' to exit:  ")
    return keyword

# def user_display():
#     get_quotes()
#     valid = 0
#     go_to_next = 0
#     while not valid:
#         next_page = input("Enter 'next page' or 'done':  ")
#         if next_page == 'done':
#             valid = 1
#         elif next_page == 'next page':
#             go_to_next = 1
#             #go to next page
#         else: print("Please enter a valid response")
#     return 0


main()