from dotenv.main import find_dotenv
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
KEY = os.environ.get('FAVQ')

url_qotd = 'https://favqs.com/api/qotd'

url_quotes = 'https://favqs.com/api/quotes'
headers = {'Content-Type': 'application/json',
            'Authorization': F'Token token={KEY}'
          }


# V1
def get_quote():
  try:
    response = requests.get(url_qotd, headers=headers)
    json = response.json()
    print(json)
  except requests.exceptions.RequestException as e:  
      raise SystemExit(e)

# V2 
def get_quotes():
  keyword = input("What would you type of quotes would you like to look for?")
  print(keyword)
  try:
    response = requests.get(url_quotes, headers=headers, params={'filter': keyword })
    json = response.json()
    return_str = ""
    for q in json['quotes']:
      return_str += F"{q['body']} \n {q['author']} \n \n"
    print(return_str)
  except requests.exceptions.RequestException as e:  
      raise SystemExit(e)



get_quotes()