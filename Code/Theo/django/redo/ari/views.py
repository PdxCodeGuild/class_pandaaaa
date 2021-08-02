import ari
from ari.models import Document
from django.core.files.base import File
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from .forms import DocumentForm
from .ari import ari_calc
import os
# from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        # print('here')
        if form.is_valid():
            form.save()
            doc = Document.objects.latest('uploaded_at')
            doc_location = str(doc.document) 
            ari_num = ari_calc(doc_location)
            print(type(ari_num))
            return render(request, 'ari/results.html', {'ari_num' : ari_num} )
        else:
            return HttpResponse('Invalid form')
    else :
        form = DocumentForm()

    return render(request, 'ari/index.html', {'form' : form})

def results(request,ari_num=0):
    return HttpResponse(ari_num)
    # return render(request, 'ari/results.html', {'ari_num' : ari_num})
