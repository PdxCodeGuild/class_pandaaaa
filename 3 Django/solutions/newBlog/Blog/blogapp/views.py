from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost
from django.contrib.auth import authenticate, login, logout
User = get_user_model()

def home(request): 
    if request.user: 
        posts = BlogPost.objects.all()
        context = {
            'posts':posts
        }
        return render(request, 'blogapp/home.html', context)
    else: 
        return HttpResponse('you need to log in')
# views for accounts
def user_login(request): 
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None: 
            print('user', user.id) 
            login(request, user)
        return redirect('blogapp:home')
    return render(request, 'blogapp/login.html')

def user_logout(request):
    logout(request)
    return redirect('blogapp:login')

def register(request): 
    if request.method =='POST':
        new_user = User(
            email= request.POST['email'],
            username=request.POST['username']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        login(request, new_user)
        return redirect('blogapp:profile', new_user.pk)
    return render(request, 'blogapp/register.html')

def profile(request, pk): 
    #get all of a users posts and display here
    user_posts = BlogPost.objects.filter(user = request.user.id)
    print(user_posts)
    context = {
        'user_posts': user_posts
    }
    return render(request, 'blogapp/profile.html', context)

def create(request):
    if request.method=='POST':
        body = request.POST['body']
        title = request.POST['title']
        # new_post = BlogPost(
        #     body= body,
        #     title = title,
        #     user = request.user
        # )
        # new_post.save()
        new_post = BlogPost.objects.create(
            body= body,
            title = title,
            user = request.user            
        )
        return redirect('blogapp:profile', request.user.id)
    return render(request, 'blogapp/create.html')

def edit_post(request, id):
    if request.method == "GET":
        post = BlogPost.objects.get(id=id)
        context = {
            'post': post
        }
        return render(request, 'blogapp/edit.html', context)

    if request.method == "POST":
        post = BlogPost.objects.get(id=id)
        post.body = request.POST['body']
        post.title = request.POST['title']
        post.save()

        return redirect('blogapp:profile', request.user.id)