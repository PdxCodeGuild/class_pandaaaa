from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import Priority, ToDoItem
from .forms import ToDoForm

# Create your views here.

def index(request):
    if request.method == 'GET':
        tasks = ToDoItem.objects.all()
        return render(request, 'index.html', {'tasks':tasks})
    else:
        return Http404()

def new_task(request):
        if request.method == 'POST':
            todo_form = ToDoForm(request.POST)
            if todo_form.is_valid():
                todo_form.save()
                newform = ToDoForm()
                return render(request, 'new_task.html', {'todo_form': newform})
        if request.method == 'GET':
            todo_form = ToDoForm()
            return render(request, 'new_task.html', {'todo_form': todo_form})

def delete_task(request,pk=-1):
    if pk == -1:
        return Http404()
    task = ToDoItem.objects.get(pk)
    task.delete()
    return index(request)