from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import TodoModel
from .forms import TodoForm

# Create your views here.
def home(request):
    # my_todos = TodoModel.objects.filter(published_date__lte=timezone.now()).order_by('-due_date')
    my_todos = TodoModel.objects.filter(startdate__lte=timezone.now()).order_by('duedate')
    my_todos = my_todos.filter(completed=False)

    # my_todos = TodoModel.objects.filter(startdate__lte=timezone.now()).order_by('duedate')
    context = {
        'todos': my_todos,
    }
    return render(request, 'todo_app/home.html', context)

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
    # form = TodoForm(request.POST)
    # if form.is_valid():
    #     todo = form.save(commit=False)
    # context = {
    #     'my_form':form
    # }
    print('here')
    if request.method == 'POST': 
        form = TodoForm(request.POST)
        print('here')
        if form.is_valid():
            print('was valid')
            form.save()
            return home(request)
    form = TodoForm() # create a new blank form
    context = {
        'my_form':form
    }
    return render(request, 'todo_app/add.html', context)