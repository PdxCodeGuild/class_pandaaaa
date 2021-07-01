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


# prog main
def main():
    joke_search()
    return 0



# This function makes a request from the url for a dad joke in JSON
def joke_request(): 
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers = {'Accept' : 'application/json'})#send a get request
    # data = response.json()
    data = json.loads(response.text)
    print(data)
    return data['joke']



# This function makes a request from the url for a dad joke in JSON
# The function also passes a search term to the get function as well
def joke_request_search(to_search): 
    url = 'https://icanhazdadjoke.com/search'
    payload = {'term': to_search}
    response = requests.get(url, headers = {'accept' : 'application/json'}, params = payload)#send a get request
    # data = response.json()
    data = json.loads(response.text)
    return data



#This function splits the argument into a question and answer. 
#The return will be: ['joke','answer']
def joke_split(joke_str):
    split = False 
    for i in joke_str:
        if i == '?':
            temp = joke_str.split('?')
            # if temp[0][-1] == '"': #Need a fix for strings like: "Dad, I'm cold.""Go stand in the corner, I hear it's 90 degrees
                # temp[-1]
            temp[0] += '?'
            return temp
        if i == '.':
            temp = joke_str.split('.')
            temp[0] += '.'
            return temp



#this function is used to search for jokes containing a word
#this function asks for user input between each joke`
def joke_search():
    again = 'y'
    while(again != 'x'):
        search_for = input('What word do you want to be included in your joke?')
        jokes = joke_request_search(search_for)
        print('\nTotal jokes found: ' + str(jokes['total_jokes']) + '\n')
        
        count = 1
        next = 'x'
        for i in jokes['results']:
            temp = joke_split(i['joke'])
            print('Joke number: ' + str(count) + '.')
            print('\n' + temp[0] + '\n')
            time.sleep(1)
            print('\n' + temp[1] + '\n')
            time.sleep(1)
            count += 1
            next = input('Enter x to exit or press enter for the next joke')
            if(next == 'x'):
                return 0
            elif(next == 'n'):
                continue
        again = input('Would you like to search for more jokes? Enter x to exit')
main()