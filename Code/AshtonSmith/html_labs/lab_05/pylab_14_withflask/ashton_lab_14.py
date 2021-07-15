# Ashton Smith
# Lab 14: Dad Joke API
# Use the Dad Joke API to get a dad joke and display it to the user. 
# You may want to also use time.sleep to add suspense.

# Part 1
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. 
# This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary.
# Get the joke out of the dictionary and show it to the user.

# Part 2
# Add the ability to "search" for jokes using another endpoint.
# Create a REPL that allows one to enter a search term and go through jokes one at a time. 
# You can also add support for multiple pages.
import requests
import json
import string
import time
import string

# prog main
def main():
    joke_search('the')
    return 0



# This function makes a request from the url for a dad joke in JSON
def joke_request(): 
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers = {'Accept' : 'application/json'})#send a get request
    data = json.loads(response.text)
    print(data)
    return data['joke']



# This function makes a request from the url for a dad joke in JSON
# The function also passes a search term to the get function as well
def joke_request_search(to_search): 
    url = 'https://icanhazdadjoke.com/search'
    payload = {'term': to_search}
    response = requests.get(url, headers = {'accept' : 'application/json'}, params = payload)#send a get request
    data = json.loads(response.text)
    return data



#This function splits the argument into a question and answer. 
#The return will be: ['joke','answer']
def joke_split(joke_str):
    split = False 
    for i in joke_str:
        if i == '?':
            temp = joke_str.split('?')
            temp[0] += '?'
            return temp
        if i == '.':
            temp = joke_str.split('.')
            temp[0] += '.'
            return temp



#this function is used to search for jokes containing a word
#this function asks for user input between each joke`
def joke_search(search_for):
        joke_list = []
        jokes = joke_request_search(search_for)
        print('\nTotal jokes found: ' + str(jokes['total_jokes']) + '\n')
        temp = []
        for i in jokes['results']:
            temp_list = []
            temp = joke_split(i['joke'])
            for j in temp:
                j = j.replace('.','*0')
                j = j.replace(',','*1')
                j = j.replace('!','*2')
                j = j.replace('?','*3')
                j = j.replace("'",'*4')
                temp_list.append(j)
            joke_list.append(temp_list)
        return joke_list

# main()

