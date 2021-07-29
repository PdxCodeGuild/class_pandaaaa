from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Person
from .forms import ProfileForm
# Create your views here.

def home(request):
  persons = Person.objects.all()
  context = { 
    'persons': persons
  }
  return render(request, 'phone_app/home.html', context) 

def profile(request, pk):
  person = Person.objects.get(pk=pk)
  form = ProfileForm(request.POST or None, instance=person )
  if request.method == "POST":
    if form.is_valid():
      form.save()
      return redirect('home')
  


  return render(request, 'phone_app/profile.html', {'form': form})