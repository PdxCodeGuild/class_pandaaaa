from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import json
# import the Todo model from the models file
from .models import Todo

# rendering template
def todo_list(request):
    return render(request, 'todos/list.html')

# getting list from database, sending as JSON response
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

# handling post request to save new todo in database
@login_required
def add_todo(request):
    print(request.body)
    data = json.loads(request.body)
    newTask = Todo(title=data['name'], text=data['description'], status=False)
    newTask.save()
    return HttpResponse('Ok!')
