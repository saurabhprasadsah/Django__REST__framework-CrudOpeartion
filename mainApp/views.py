from django.shortcuts import render,HttpResponse
from .models import Employee
from rest_framework.renderers import JSONRenderer 
from .serializers import EmployeeSerializer

# Create your views here.
def homePage(Request):
    return render(Request,'index.html')


def getPage(Request):
    data =Employee.objects.all()
    dataSerializer = EmployeeSerializer(data, many=True)
    return HttpResponse(JSONRenderer().render(dataSerializer.data), content_type ="application/json")