import random
from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/hello')
def index(): 
    return 'hello world'


# # unique route with string parameter
@app.route('/<string:name>')
def hello(name):
    return 'hello, ' + name
# app.run(debug=True)

# # unique route with integer parameter
@app.route('/<int:id>')
def numbers(id): 
    return "hello, " + str(id)

@app.route('/emoticon')
def emoticon():
    eyes = random.choice([':', ';', '='])
    nose = random.choice(['', '-', 'o'])
    mouth = random.choice([')', '(', ']', 'D'])
    emoticon = eyes + nose + mouth
    return render_template('emoticon.html', emoticon=emoticon)
phrases = []
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        form_data = request.form['input_text']
        phrases.append(form_data)
        print(phrases)
        return render_template('form.html', phrases = phrases)
    else:
        return render_template('form.html', phrases=phrases)

# unique route with multiple parameters
@app.route('/<string:name>/<int:id>')
def profile(name, id): 
    return "hello, " + name + ", your id is:" + str(id)

@app.route('/onlyget', methods=['GET'])
def get_only():
    return 'You can only get this webpage'

@app.route('/home')
def home():
    my_name ='Sarah Beth'
    fruits = ['papayas', 'bananas', 'oranges', 'apples']
    return render_template('home.html', name=my_name, fruits=fruits)

app.run(debug=True)
