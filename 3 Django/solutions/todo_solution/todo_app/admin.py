from django.contrib import admin

from . import models

admin.site.register(models.Todo)
admin.site.register(models.Priority)
admin.site.register(models.User)
