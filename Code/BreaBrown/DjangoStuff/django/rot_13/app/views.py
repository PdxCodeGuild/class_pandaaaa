from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cypher

# Create your views here.

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

    def convert(self, input):
        output = ''
        msg = list(input)
        for index, value in enumerate(msg):
            msg[index] = self.rot13_dict[value]
        output = output.join(msg)
        # output.join(msg)
        return output


def index(request):
    if request.method == 'POST':
        string = request.POST['input']
        # print(string)
        encryptor = Encryptor()
        cypher = encryptor.convert(string)
        print(cypher)
        context = {
            'encrypted_msg': cypher
        }
        return render(request, 'app/index.html', context)
    else: 
        return render(request, 'app/index.html')