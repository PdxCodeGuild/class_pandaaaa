from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
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
    my_option = request.POST.get('delete_button')
    if my_option == 'Delete':
         return HttpResponseRedirect("/delete_profile/"+str(pk))
    if form.is_valid():
      form.save()
      return home(request)
  return render(request, 'phone_app/profile.html', {'form': form})


  
def make_profile(request):
  if request.method == "POST":
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
  else:
    form = ProfileForm()
  return render(request, 'phone_app/make_profile.html', {'form': form})



def delete_profile(request, pk):
  person = Person.objects.get(pk=pk)
  print('delete profile')
  if request.method == "POST":
    my_option = request.POST.get('confirm_button')
    if my_option == 'Yes':
      person.delete()
      return HttpResponseRedirect('/')
  return render(request, 'phone_app/delete_profile.html')