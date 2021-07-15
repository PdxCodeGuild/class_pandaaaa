from flask import Flask, render_template, redirect, request
import ashton_lab_14 as joke_getter
app = Flask(__name__)
import csv


@app.route('/', methods=['GET', 'POST'])
def index():
    search_term = request.form.get("search")
    jokes = []
    if(search_term):
        jokes = joke_getter.joke_search(search_term)
    return render_template('index.html', jokes=jokes)


@app.route('/search/<string:search_term>', methods=['GET', 'POST'])
def search(search_term):
    jokes = []
    print('search term ------------------------------------------------')
    print(search_term)

    # search_term = request.form.get("search")
    if(search_term):

        search_term = request.form.get("search")
        jokes = joke_getter.joke_search(search_term)
        search_term = ''
        return render_template('index.html', jokes=jokes)

    return render_template('index.html', jokes=jokes)

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

@app.route('/savejoke/<string:joke1>' , methods=['GET', 'POST'] )
def save_joke_1(joke1):
    search_term = request.form.get("search")
    jokes = []
    if(search_term):
        jokes = joke_getter.joke_search(search_term)
        url = ('/search/' + str(search_term))
        print(url)
        return redirect(url)
    # search_term = request.form.get("search")
    # jokes = []
    # if(search_term):
    #     jokes = joke_getter.joke_search(search_term)
    #     url = ('/search/' + str(search_term))
    #     print(url)
    #     return redirect(url)

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

def load_joke():
    with open('favorites.csv') as f:
        lines = f.read().split('\n')
    jokes = []
    header = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        jokes.append(row)
        # print('-------jokes\n')
        # print(jokes)

    return jokes


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