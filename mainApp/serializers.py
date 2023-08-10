from rest_framework import serializers
from .models import Employee
# Create your serializer here.

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name= serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=20)
    phone =serializers.CharField(max_length=15)
    dsg = serializers.CharField(max_length=50)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=30)
    state = serializers.CharField(max_length=30)
