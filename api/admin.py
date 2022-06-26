from django.contrib import admin

# Register your models here.
from .models import Profile

@admin.register(Profile)
class Admin(admin.ModelAdmin):
    list_display =  ['id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'rdoc']

    
