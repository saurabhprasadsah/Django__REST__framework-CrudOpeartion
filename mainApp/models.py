from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    phone =models.CharField(max_length=15)
    dsg = models.CharField(max_length=50)
    salary = models.IntegerField()
    city = models.CharField(max_length=30, default="", null= True, blank= True)
    state = models.CharField(max_length=30, default="", null= True, blank= True)




