from flask import Flask
import labs.atm

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/<string:name>')
def hello(name):
    return f'hello {name}'

@app.route('/<string:name>/<int:id>')
def profile(name,id):
    return f' hello {name}, your ID is: {str(id)}'

@app.route('/emoticon')
def emoticon():
    

app.run(debug=True)

if __name__ == '__main__':
    index()