from django.contrib import admin
from .models import api

class TodoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

# Register your models here.

admin.site.register(api, TodoAdmin)
