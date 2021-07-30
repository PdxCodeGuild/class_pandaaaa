from dotenv.main import find_dotenv
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
KEY = os.environ.get('FAVQ')
# Quote of the day URL
url_qotd = 'https://favqs.com/api/qotd'
# List of Quotes URL
url_quotes = 'https://favqs.com/api/quotes'

headers = {'Content-Type': 'application/json',
            'Authorization': F'Token token={KEY}'}


#---------------------------------------------------------- V1 -----------------------------------------------------------------------------------------
def get_quote():
  try:
    response = requests.get(url_qotd, headers=headers)
    json = response.json()
    quote = json['quote']
    print(F"\"{quote['body']}\" \n {quote['author']} \n \n ")
  except requests.exceptions.RequestException as e:  
      raise SystemExit(e)

#---------------------------------------------------------- V2 -----------------------------------------------------------------------------------------

# This function searches the API using the keyword passed into it then filters and prints the results
# also returns False if there are no more quotes for the given keyword
def get_quotes(keyword, page=1):
  try:
    response = requests.get(url_quotes, headers=headers, params={'filter': keyword, 'page': page })
    json = response.json()
    return_str = ""
    for q in json['quotes']:
      author= q['author'] if 'author' in q else ''
      return_str += F"\"{q['body']}\" \n {author} \n \n"
    print(return_str)
    # if return_str == 'No quotes found': # Why doesn't this return True?
    if json['quotes'][0]['body'] == 'No quotes found':
      return True
    else:
      return json['last_page']
  except requests.exceptions.RequestException as e:  
      raise SystemExit(e)

# This functions takes an input from a user then runs the appropriate function based on the user's input
# and then takes the return from get_quotes() to evaluate what to ask the user
def question_looper():
  counter = 1
  breaker = True
  keyword = ''
  last_page = False
  while breaker:
    # this catches if the counter goes past 25 because there are no quotes returned after 25 but the last_page property doesn't return True on page 25
    if last_page or counter > 25:
      print(F" There are no more quotes for {keyword}.")
      counter = 1
      last_page = False
    elif counter == 1:
      keyword = input(F" give me a keyword to search for quotes with. \n enter R for a random quote or E to Exit \n").lower()
      if keyword == "e":
        breaker = False
      elif keyword == "r":
        get_quote()
      else:
        last_page = get_quotes(keyword)
        counter += 1
    elif counter <= 25:
      q2 = input(F" Would you like to see more quotes for {keyword}? \nY = Yes, N = No, E = Exit \n").lower()  
      if q2 == "e":
        breaker = False
      elif q2 == "y":
        last_page = get_quotes(keyword, counter)
        counter += 1
      elif q2 == "n":
        counter = 1
      else:
        print("sorry that response isn't recognized\n")
  exit(0)

question_looper()