from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from .models import Person

def myview(request):
    contacts = Person.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'phoneapp/index.html', context)

def mycreate(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    mymodel = Person(name=name, phone=phone, email=email)
    mymodel.save()
    return HttpResponseRedirect(reverse('phoneapp:myview'))

def contact(request, pk):
    contact = Person.objects.get(pk=pk)
    context = {
        'contact':contact
    }
    return render (request, 'phoneapp/contact.html', context)

def edit(request, pk):
    contact = Person.objects.get(pk=pk)
    context = {
        'contact':contact
    }
    if request.method == "POST":
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.save()
        print(request)
        return HttpResponseRedirect(reverse('phoneapp:myview'))
    return render (request, 'phoneapp/edit.html', context)

def delete(request,pk):
    contact = Person.objects.get(pk=pk)
    contact.delete()
    return HttpResponseRedirect(reverse('phoneapp:myview'))