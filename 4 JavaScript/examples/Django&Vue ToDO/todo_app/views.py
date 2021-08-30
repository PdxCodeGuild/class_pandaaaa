from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import json
# import the Todo model from the models file
from .models import Todo

def todo_list(request):
    return render(request, 'todos/list.html')

def todos(request):
    todos = Todo.objects.order_by('-created_at')
    all_todos= []
    for todo in todos: 
        all_todos.append(
            {
                'name': todo.title,
                'text': todo.text,
                'status': todo.status,
                'created_at': todo.created_at,
                'priority': todo.priority
            }
        )
    return JsonResponse({'todos': all_todos})

# view to get retrieve a specific todo from the database and send it to the 'todos/detail.html' view
def details(request, id):
    todo = Todo.objects.get(id = id)
    return render(request, 'todos/detail.html', {"todo": todo})


@login_required
def add_todo(request):
    print(request.body)
    data = json.loads(request.body)
    newTask = Todo(title=data['name'], text=data['description'], status=False)
    newTask.save()
    return HttpResponse('Ok!')

# view to remove a specific todo from the database specified by its id
def remove_todo(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    
    return redirect('list')

# helper function for updating a todo. gets the todo info specified by the id and redirects to its detail page
def update_todo(request, id):
    todo = Todo.objects.get(id = id)
    return redirect('details', todo.id)

# view to update a todo in the databse specified by its id
def update(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'todos/update.html', {'todo': todo})
    elif request.method == 'POST':
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        if (request.POST['status'] == 'False'):
            todo.status = False
        else:
            todo.status = True
        todo.save()
        return redirect('details', todo.id)

# mark a todo as done
def mark_done(request, id):
    todo = Todo.objects.get(id = id)
    todo.status = True
    todo.save()

    return redirect('details', todo.id)