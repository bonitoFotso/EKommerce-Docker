from django.contrib import admin
from .models import *

class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')

admin.site.register(Client, ClientModelAdmin)