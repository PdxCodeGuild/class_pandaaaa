from django.contrib import admin
from .models import CustomUser
from chirp.models import Cheep

# Register your models here.

class CheepInline(admin.TabularInline):
    model = Cheep

class UserAdmin(admin.ModelAdmin):
    inlines = [CheepInline]
    class Meta:
        model = CustomUser

admin.site.register(CustomUser, UserAdmin)
