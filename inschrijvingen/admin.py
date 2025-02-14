from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Inschrijving, Workshop

admin.site.register(Inschrijving)
admin.site.register(Workshop)  
