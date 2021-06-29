# Lab 15: Quotes API
# For this lab we'll be using the Favqs Quotes API to first get a random quote,
#  and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests library.

# Version 1: Get a Random Quote
# The URL to get a random quote is https://favqs.com/api/qotd, 
# send a request here, parse the JSON in the response into a python dictionary, i
# and show the quote and the author.
import requests
import json


#prog main
def main():
    # request_quote()

    request_quote_search()
    return 0



#this function quests a quote
def request_quote():
    url = 'https://favqs.com/api/qotd'
    response = requests.get(url, headers = {'Accept' : 'application/json'})#send a get request
    # data = response.json()
    data = json.loads(response.text)
    print(data)


def request_quote_search():
    page = '1'
    term = 'what'
    # url = f'https://favqs.com/api/quotes?page=<{page}>&filter=<{term}>'
    # url = 'https://favqs.com/api/quotes?page=1&filter=what'
    # url = 'https://favqs.com/api/quotes'#/?filter=funny'
    url = 'https://favqs.com/api/quotes/?filter=funny'
    headers = {'Authorization': 'Token token="5b8c456532d65b17d851bba193977bf9"'}
    # print (url)
    response = requests.get(url, headers)# = {'Accept' : 'application/json'})#, params= {'term':'thou'})#send a get request
    # data = response.json()
    # 9
    # data = json.loads(response.text)
	# 5b8c456532d65b17d851bba193977bf9
    # print(data)
    print(response)


# An app token is required to access our API (except for the Quote of the Day).

# For authorized API calls, pass your access token in via the header:

# Authorization: Token token="YOUR_APP_TOKEN"
# For example,

# $ curl -H 'Authorization: Token token="YOUR_APP_TOKEN"'
# Note:  This format will not work:

# Authorization: "YOUR_APP_TOKEN"
main()










# Version 2: List Quotes by Keyword
# The Favqs Quote API also supports getting a list of quotes associated with a given keyword 
# https://favqs.com/api/quotes?page=<page>&filter=<keyword>. 
# Prompt the user for a keyword, list the quotes you get in response, 
# and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.

# > enter a keyword to search for quotes: nature
# 25 quotes associated with nature - page 1
# <list of quotes>
# > enter 'next page' or 'done': next page
# 25 quotes associated with nature - page 2
# <list of quotes>
# > enter 'next page' or 'done': done
# > enter a keyword to search for quotes:
# This API endpoint requires an API key be included in a request header. You can find documentation of specifying request headers here and documentation on authorization with the Favqs API here under "Authorization".

# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
# Other Quote APIs
# Programming Quotes
# Quotes Garden
# get random quote https://quote-garden.herokuapp.com/quotes/random
# get quotes by keyword https://quote-garden.herokuapp.com/quotes/search/<keyword/