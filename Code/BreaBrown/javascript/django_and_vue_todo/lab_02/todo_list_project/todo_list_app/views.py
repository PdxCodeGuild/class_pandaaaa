from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Task

def index(request):    
    completed_tasks = Task.objects.filter(complete = True).order_by('-date_completed')
    incomplete_tasks = Task.objects.filter(complete = False).order_by('date_created')
    context = {
        'completed_tasks': completed_tasks,
        'incomplete_tasks': incomplete_tasks,
    }
    return render(request, 'todo_list/index.html', context)

def new(request):
    task_title = request.POST['task_title']
    task_detail = request.POST['task_detail']
    Task.objects.create(task_title=task_title, task_detail=task_detail, date_created=timezone.now(), complete=False)
    return HttpResponseRedirect(reverse('todo_list_app:index'))

def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse('todo_list_app:index'))

def complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = False if task.complete else True
    task.date_completed = timezone.now() if task.complete else None
    task.save()
    return HttpResponseRedirect(reverse('todo_list_app:index'))