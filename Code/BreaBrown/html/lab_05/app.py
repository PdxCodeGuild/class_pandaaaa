from flask import Flask, render_template, request

class Encryptor:
    def __init__(self):
        self.rot13_dict = { 'a': 'n',
        'b': 'o',
        'c': 'p',
        'd': 'q',
        'e': 'r',
        'f': 's',
        'g': 't',
        'h': 'u',
        'i': 'v',
        'j': 'w',
        'k': 'x',
        'l': 'y',
        'm': 'z',
        'n': 'a',
        'o': 'b',
        'p': 'c',
        'q': 'd',
        'r': 'e',
        's': 'f',
        't': 'g',
        'u': 'h',
        'v': 'i',
        'w': 'j',
        'x': 'k',
        'y': 'l',
        'z': 'm'
        }
    def convert(self, message):
        message = list(message)
        output = ''
        for index, value in enumerate(message):
            message[index] = self.rot13_dict[value]

        for letter in message:
            output += letter        

        return output

app = Flask(__name__)
@ app.route('/', methods = ['GET', 'POST'])

def index():
    if request.method == 'POST':
        encryptor = Encryptor()
        output = encryptor.convert(request.form["msg"])
        return render_template('results.html', user_dict=request.form, output=output)
    else:
        return render_template('index.html')

app.run(debug=True)    