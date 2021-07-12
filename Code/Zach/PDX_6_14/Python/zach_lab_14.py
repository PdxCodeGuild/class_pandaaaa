#Zach Watts
#Lab 14: Dad Joke API  

import requests
import json
import random

#--------------------------------------PART 1--------------------------------------#

response = requests.get('https://icanhazdadjoke.com/')
data = response.text
with open('dadjokes.json') as file:
  text = file.read()
  data_ = json.loads(text)
  jokes = data_["jokes"]

jokes_lst = []

for item in jokes:
  for k, v in item.items():
    if k == 'question':
        jokes_lst.append(v + " " + item["answer"])
    if k == 'joke':
      jokes_lst.append(v)

#print(random.choice(jokes_lst))

#-------------------------------------PART 2--------------------------------------#
def main():
    get_jokes()
    exit()

def get_jokes(term=None,limit=20, page=1):
    endpoint = 'https://icanhazdadjoke.com/search'
    term = input('Enter a search term:  ')
    params = {
      'page': page,
      'limit': limit,
      'term': term}
    headers = {'Accept': 'application/json'}
    response = requests.get(endpoint + "?" + term, params=params, headers=headers)
    print(response.json())
    exit()

main()