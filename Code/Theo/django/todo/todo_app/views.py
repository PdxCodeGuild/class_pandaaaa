from django.urls import reverse_lazy
from django.http.response import Http404
from django.shortcuts import render
from .models import Priority, ToDoItem
from .forms import ToDoForm
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
# Create your views here.

class TaskList(ListView):
    model= ToDoItem
    template_name = 'index.html'
    context_object_name = 'tasks'

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