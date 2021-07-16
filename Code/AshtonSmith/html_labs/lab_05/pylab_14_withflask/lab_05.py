#Ashton Smith
#This program is uses lab14, the dad joke finder to make a flask program. The program allows the user to search for and save dad jokes.
# from Code.AshtonSmith.html_labs.lab_05.pylab_14_withflask.ashton_lab_14 import joke_request_random
from flask import Flask, render_template, redirect, request
import random_word
import ashton_lab_14 as joke_getter
app = Flask(__name__)
import csv

#this route is the index page - the function is used to get a list of jokes from joke_getter
@app.route('/', methods=['GET', 'POST'])
def index():

    search_term = request.form.get("search")
    jokes = []
    if(search_term):
        jokes = joke_getter.joke_search(search_term)
    else:
        jokes = joke_getter.joke_search_random()
        if jokes == None:
            jokes = []
    return render_template('index.html', jokes=jokes)



#this route is used to display a given search result - the function is used to get a list of jokes from joke_getter
@app.route('/search/<string:search_term>', methods=['GET', 'POST'])
def search(search_term):
    jokes = []
    if(search_term):
        search_term = request.form.get("search")
        jokes = joke_getter.joke_search(search_term)
        search_term = ''
        return render_template('index.html', jokes=jokes)
    return render_template('index.html', jokes=jokes)



#this route is used to save a joke. the route inclues the first part of the joke as well as the second part.
#there is a seperate function for jokes with 1 part: save_joke1(joke1)
#the function takes joke1 and joke2 from the route and first checks if the joke is already saved and sets a boolean if it is.
#if the joke isnt saved it will be added to the csv like this: \njoke1, joke2
#the function will then get the jokes from the .csv file
@app.route('/savejoke/<string:joke1>/<string:joke2>', methods=['GET', 'POST'] )
def save_joke(joke1, joke2):
    search_term = request.form.get("search")
    jokes = []
    if(search_term):
        jokes = joke_getter.joke_search(search_term)
        url = ('/search/' + str(search_term))
        print(url)
        return redirect(url)
    found = False
    #check if already saved
    with open('favorites.csv','rt') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            for field in row:
                if field == joke1:
                    print('already saved')
                    found = True
    if(not found):
        with open('favorites.csv','a') as f:
            f.write('\n' + str(joke1) + ',' + str(joke2))
    joke_list = load_joke()
    return render_template('index.html', jokes= joke_list)



#this route is used to display a given search result - the function is used to get a list of jokes from joke_getter
@app.route('/savejoke/<string:joke1>' , methods=['GET', 'POST'] )
def save_joke_1(joke1):
    search_term = request.form.get("search")
    jokes = []
    if(search_term):
        jokes = joke_getter.joke_search(search_term)
        url = ('/search/' + str(search_term))
        print(url)
        return redirect(url)
    found = False
    #check if already saved
    with open('favorites.csv','rt') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            for field in row:
                if field == joke1:
                    print('already saved')
                    found = True
    #append to csv
    if(not found):
        with open('favorites.csv','a') as f:
            f.write('\n' + str(joke1))
    joke_list = load_joke()
    return render_template('index.html', jokes= joke_list)



#this function is used to load a list of functions from the .csv file
def load_joke():
    with open('favorites.csv') as f:
        lines = f.read().split('\n')
    jokes = []
    header = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        jokes.append(row)
    return jokes



#this route is used to display favorite jokes from the .csv file
@app.route('/favorites', methods=['GET', 'POST'])
def favorite_jokes():
    search_term = request.form.get("search")
    if(search_term):
        jokes = joke_getter.joke_search(search_term)
        url = ('/search/' + str(search_term))
        print(url)
        return redirect(url)
    joke_list = load_joke()
    return render_template('index.html', jokes= joke_list)



app.run(debug=True)