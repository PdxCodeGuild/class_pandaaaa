from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse



# def myview(request):
#     contacts = Person.objects.all()
#     context = {
#         'contacts': contacts
#     }
#     return HttpResponse('hello world!') #render(request, 'phoneapp/index.html', context)

from django.http import HttpResponse

def myview(request):
    return HttpResponse('hello world!')