from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser

from .models import Employee
from .serializers import EmployeeSerializer

import io


# Create your views here.
def homePage(Request):
    return render(Request,'index.html')

@csrf_exempt
def createPage(Request):
    stream = io.BytesIO(Request.body)
    pythonData = JSONParser().parse(stream)
    employeeSerializer= EmployeeSerializer(data=pythonData)
    if(employeeSerializer.is_valid()):
        employeeSerializer.save()
        response={'result':"done",'message':"Record is created!"}
    else:
        response={'result':"Fail",'message':"invalid data"}
    return HttpResponse(JSONRenderer().render(response), content_type="application/json")



#get request from the serializer
#use serializer
def getPage(Request):
    data =Employee.objects.all()
    dataSerializer = EmployeeSerializer(data, many=True)
    return HttpResponse(JSONRenderer().render(dataSerializer.data), content_type ="application/json")