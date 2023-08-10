
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('employee/getPage/', views.getPage)
]
