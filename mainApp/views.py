from django.shortcuts import render,HttpResponse

# Create your views here.
def homePage(Request):
    return render(Request,'index.html')


def getPage(Request):
    return HttpResponse("Hello from the server")