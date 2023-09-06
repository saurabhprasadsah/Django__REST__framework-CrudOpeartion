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

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
#update se name
    def update(self, instance,validated_data):
        if("name" is validated_data and validated_data['name'!=""]):
             instance.main = validated_data['name']

        if("email" is validated_data and validated_data['email'!=""]):
             instance.main = validated_data['email']    

        if("phone" is validated_data and validated_data['phone'!=""]):
             instance.main = validated_data['phone']  

        if("dsg" is validated_data and validated_data['dsg'!=""]):
             instance.main = validated_data['dsg'] 

        if("salary" is validated_data and validated_data['salary'!=""]):
             instance.main = validated_data['salary'] 

        if("city" is validated_data and validated_data['city'!=""]):
             instance.main = validated_data['city']   
               
        if("state" is validated_data and validated_data['state'!=""]):
             instance.main = validated_data['state']   

        instance.save()       


        