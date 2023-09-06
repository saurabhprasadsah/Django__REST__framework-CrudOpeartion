from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
import io

# Create your views here.
def homePage(Request):
    return render(Request,'index.html')

#use decorator
@csrf_exempt
def createPage(Request):
    stream = io.BytesIO(Request.body)
    pythonData = JSONParser().parse(stream)
    temp = Employee.objects.last()
    pythonData.setdefault('id', temp.id+1)  
    employeeSerializer= EmployeeSerializer(data=pythonData)
    
    if(employeeSerializer.is_valid()):
        employeeSerializer.save()
        response={'result':"done",'message':"Record is created!"}
    else:
        response={'result':"Fail",'message':"invalid data"}

    return HttpResponse(JSONRenderer().render(response), content_type="application/json")


#get request from the serializer
#use serializer
@csrf_exempt
def getPage(Request):
    data =Employee.objects.all()
    dataSerializer = EmployeeSerializer(data, many=True)
    return HttpResponse(JSONRenderer().render(dataSerializer.data), content_type ="application/json")


def getSinglePage(Request,id):
    try:
        data =Employee.objects.get(id = id)
        dataSerializer = EmployeeSerializer(data)
        return HttpResponse(JSONRenderer().render(dataSerializer.data), content_type ="application/json")
    except:
        return HttpResponse(JSONRenderer().render({'result':"Fail", "message":"invalid id"}), content_type ="application/json")


@csrf_exempt
def deletePage(Request, id):
    try:
        data = Employee.objects.get(id =id)
        data.delete()
    except:
        pass    
    return HttpResponse(JSONRenderer().render({'result':"done", "message":"Record is delete"}), content_type ="application/json")



#update page
@csrf_exempt
def updatePage(Request):
    stream = io.BytesIO(Request.body)
    pythonData = JSONParser().parse(stream)
    try:
        emp = Employee.objects.get(id=pythonData['id'])
        employeeSerializer= EmployeeSerializer(emp, data=pythonData,partial=True)
        if(employeeSerializer.is_valid()):
            employeeSerializer.save()
            return HttpResponse(JSONRenderer().render({'result':" done", "message":"Record is updated!!!"}), content_type ="application/json")
        else:
            return HttpResponse(JSONRenderer().render({'result':"Fail", "message":"Invalid data!!!"}), content_type ="application/json")

    except:
        return HttpResponse(JSONRenderer().render({'result':"Fail", "message":"Record not found"}),content_type ="application/json")
    
#when we call the restapi then pass the value will be "search":saurabh
@csrf_exempt
def SearchPage(Request):
    stream = io.BytesIO(Request.body)
    pythonData= JSONParser().parse(stream)
    search = pythonData['search']  
    data = Employee.objects.filter(Q(name__icontains=search)|Q(email=search)|Q(phone=search)|Q(city=search)|Q(state=search)) 
    dataSerializer = EmployeeSerializer(data,many=True)
    return HttpResponse(JSONRenderer().render(dataSerializer.data), content_type ="application/json")

