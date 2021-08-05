import requests
import json 


page = input('which page do you want to see?')

response = requests.get('https://catfact.ninja/breeds', params={'page': page})


print(response.text)
# data = response.text
# data = response.json()

# cat_breeds = data['data']

# breed_list = []

# for breed in cat_breeds:
#     breed_list.append(breed['breed'])

# print(breed_list)