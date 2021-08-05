from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import BlogPost
from django.http import HttpResponse
from django.contrib.auth import get_user_model #, login_required


User = get_user_model()

def myview(request):
    myinstances = BlogPost.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'blogapp/index.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        user = request.POST['user']
        public = request.POST['Public']
        date_created= request.POST['date_created']           
        date_edited= request.POST['date_edited']
        todo = BlogPost.objects.create(title=title, body=body, user=user, public=public, date_created=date_created, date_edited=date_edited)
        return redirect('blogapp/profile.html')
    else: return render(request,'blogapp/create.html')


def profile(request, pk):
    post = BlogPost.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'profile.html', context)

def delete(request, pk):
    pass

#def edit(request, pk):
 #   pass

