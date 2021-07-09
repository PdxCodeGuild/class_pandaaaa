import requests
import json

response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
data = response.json()

# print(data['joke'])

def search_keyword():
    while True:
        user_input = input('Enter a keyword: ').lower()
        response = requests.get('https://icanhazdadjoke.com/search',params={'term':user_input}, headers={'accept': 'application/json'})
        # print(response.text)
        data = response.json()
        # print(data)
        data = data['results']
        for k in data:
            print(k['joke'])    
        page = 1    
        print(f'Page - {page}')
        nav = input('Enter "next" and "previous" to use page navigation, "quit" to exit, or "new" to search again: ').lower()
        if nav == 'next':
            page += 1
        elif nav == 'previous':
            if page == 1:
                print('User Error! Page does not exist!')   
        elif nav == "quit":
            exit()
        elif nav == "new":
            user_input = input('Enter new key term: ').lower()
            response = requests.get('https://icanhazdadjoke.com/search',params={'term':user_input}, headers={'accept': 'application/json'})
            data = response.json()
            data = data['results']
            for k in data:
                print(k['joke'])
        else:
            print('Invalid Entry!')
search_keyword()           