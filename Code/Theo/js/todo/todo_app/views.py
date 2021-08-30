from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Priority, ToDoItem
from .forms import ToDoForm
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, CreateView
# Create your views here.

class TaskList(ListView):
    model= ToDoItem
    template_name = 'index.html'
    context_object_name = 'tasks'


class JSONdata(View):
    def get(request, *args, **kwargs):
        return_tasks = []
        tasks = ToDoItem.objects.all()
        for task in tasks:
            return_tasks.append(
                {
                    'text': task.text,
                    'priority': str(task.priority),
                    'created_date': task.created_date,
                    'completed_date': task.completed_date
                }
            )
        return JsonResponse({'data':return_tasks})
    def post(request):
        pass

class TaskCreate(CreateView):
    model = ToDoItem
    template_name='edit.html'
    form_class = ToDoForm
    success_url = '..'

class TaskUpdate(UpdateView):
    model= ToDoItem
    template_name='edit.html'
    form_class = ToDoForm
    success_url = '..'

# class DeleteTask(DeleteView):
#     model = ToDoItem
#     success_url = reverse_lazy('index')