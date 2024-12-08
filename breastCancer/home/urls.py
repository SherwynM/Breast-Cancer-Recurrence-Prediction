from django.contrib import admin
from django.urls import path
from home import views 

handler404 = 'home.views.custom_404'
urlpatterns = [
    
    path("",views.index, name='home')
    
]
