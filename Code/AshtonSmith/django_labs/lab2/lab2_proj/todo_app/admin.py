from django.contrib import admin
from .models import TodoModel,Priority
# Register your models here.
admin.site.register(TodoModel)
admin.site.register(Priority)