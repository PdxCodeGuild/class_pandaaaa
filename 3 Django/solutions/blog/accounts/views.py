from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from blog_posts.models import BlogPost
User = get_user_model()

def user_register(request):
    if request.method =='POST':
        new_user = User(
            username = request.POST['username'],
            email = request.POST['email'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        login(request, new_user)

        return redirect('profile')
    return render(request, 'accounts/register.html')

def profile(request):
    posts = BlogPost.objects.filter(user = request.user)
    context = {
        'posts': posts
    }
    return render(request, 'accounts/profile.html', context)

def user_login(request):
    if request.method =='POST':
        user = authenticate(
            request, 
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None: 
            login(request, user)
            print(user.id)
            print(user.username)
            return redirect('profile')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')