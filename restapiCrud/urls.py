
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('employee/create/', views.createPage),
    path('employee/get/', views.getPage),
    path('employee/get/<int:id>', views.getSinglePage),
    path('employee/delete/<int:id>', views.deletePage),
    path('employee/search/', views.searchPage)


]
