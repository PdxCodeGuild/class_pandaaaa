from django.shortcuts import render, redirect
from .models import Shortened_Url
import random
from string import ascii_letters, digits

# Create your views here.

def generate_code():
    code = ''
    max_length = 12
    for i in range(max_length):
        code += random.choice(ascii_letters + digits)
    print(code)
    return code

def index(request):
    shortened_urls = Shortened_Url.objects.all()
    context = {
        'shortened_urls' : shortened_urls
    }
    return render(request,'index.html',context)

def save(request):
    if request.method == 'POST':
        form_url = request.POST['url']
        new_url = Shortened_Url(url = form_url,code=generate_code())
        new_url.save()
        return redirect('index')


def code(request,code):
    pass
