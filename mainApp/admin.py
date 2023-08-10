from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display=['id','name','email','phone','dsg','city', 'state', ]
    
