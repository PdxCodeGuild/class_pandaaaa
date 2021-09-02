from django.contrib import admin

from . import models
admin.site.register(models.Villain)
admin.site.register(models.Movie)

# Register your models here.
# from movies.models import Villain, Movie

# @admin.register(Villain)
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title', 'rating')

# @admin.register(Movie)
# class VillainAdmin(admin.ModelAdmin):
#     list_display = ('name', 'movie')
