from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic.base import View
from .models import TodoModel
from .forms import TodoForm
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views import generic
# Create your views here.
def home(request):
    my_todos = TodoModel.objects.filter(startdate__lte=timezone.now()).order_by('duedate')
    my_todos = my_todos.filter(completed=False)
    context = {
        'todos': my_todos,
    }
    if request.method== "POST":
        mark_complete(request.POST.get('done_btn'))
    return render(request, 'todo_app/home.html', context)



def completed(request):
    my_todos = TodoModel.objects.filter(startdate__lte=timezone.now()).order_by('duedate')
    my_todos = my_todos.filter(completed=True)
    context = {
        'todos': my_todos,
    }
    if request.method== "POST":
       mark_complete(request.POST.get('done_btn'))
    return render(request, 'todo_app/home.html', context)



def high(request):
    my_todos = TodoModel.objects.filter(startdate__lte=timezone.now()).order_by('duedate')
    my_todos = my_todos.filter(priority='1')
    my_todos = my_todos.filter(completed=False)
    context = {
        'todos': my_todos,
    }
    if request.method== "POST":
       mark_complete(request.POST.get('done_btn'))
    return render(request, 'todo_app/home.html', context)



def medium(request):
    my_todos = TodoModel.objects.filter(startdate__lte=timezone.now()).order_by('duedate')
    my_todos = my_todos.filter(priority='2')
    my_todos = my_todos.filter(completed=False)
    context = {
        'todos': my_todos,
    }
    if request.method== "POST":
       mark_complete(request.POST.get('done_btn'))
    return render(request, 'todo_app/home.html', context)
    


def low(request):
    my_todos = TodoModel.objects.filter(startdate__lte=timezone.now()).order_by('duedate')
    my_todos = my_todos.filter(priority='3')
    my_todos = my_todos.filter(completed=False)
    context = {
        'todos': my_todos,
    }
    if request.method== "POST":
       mark_complete(request.POST.get('done_btn'))
    return render(request, 'todo_app/home.html', context)



class TodoUpdate(UpdateView):
    model = TodoModel
    fields= ['title',
            'details',
            'startdate',
            'duedate',
            'completed',
            'priority',]
    template_name_suffix = '_update_form'
    success_url = '/'



class TodoDetailed(generic.DetailView):
    model = TodoModel
    context_object_name = 'todo'



def mark_complete(pk):
    todo = get_object_or_404(TodoModel, pk=pk)
    todo.completed = not(todo.completed)
    todo.save()



def delete(request,pk):
    todo = get_object_or_404(TodoModel, pk=pk)
    context = {
        'todo':todo
    }
    if request.method== "POST":
        #delete form
        if(request.POST.get('option_btn') == 'yes'):
            todo.delete()
        return HttpResponseRedirect('/')
    return render(request, 'todo_app/delete.html', context)



def add(request):
    if request.method == 'POST': 
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = TodoForm() # create a new blank form
    context = {
        'my_form':form
    }
    return render(request, 'todo_app/add.html', context)