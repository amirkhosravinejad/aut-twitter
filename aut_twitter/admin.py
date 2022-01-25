from django.contrib import admin
<<<<<<< HEAD
#from .models import api

#class TodoAdmin(admin.ModelAdmin):
    #list_display = ('username', 'password')

# Register your models here.

#admin.site.register(api, TodoAdmin)
=======
from .models import api

class TodoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

# Register your models here.

admin.site.register(api, TodoAdmin)
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493
