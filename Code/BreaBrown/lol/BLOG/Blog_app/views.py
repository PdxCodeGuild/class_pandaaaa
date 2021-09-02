from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

# register
# login
# profile

def register(request):
    return render(request, 'register.html')

def login(request):
    print('hello')
    if request.method == 'POST':
        print('hello post')
        print(request.POST['email'])
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def logout(request):
    return redirect('login')