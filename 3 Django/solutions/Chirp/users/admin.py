from django.contrib import admin
from .models import CustomUser
from chirp.models import Chirp

# Register your models here.

class ChirpInline(admin.TabularInline):
    model = Chirp

class UserAdmin(admin.ModelAdmin):
    inlines = [ChirpInline]
    class Meta:
        model = CustomUser

admin.site.register(CustomUser, UserAdmin)
