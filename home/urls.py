from django.contrib import admin
from django.urls import path
from home import views
admin.site.site_header = "Anish is learning Admin"
admin.site.site_title = "Anish is learning Admin Portal"
admin.site.index_title = "Welcome to Anish is learning Researcher Portal"
urlpatterns = [
        path("", views.index, name='home'),
        path("about", views.about, name='about') ,
        path("services", views.services, name='services') , 
        path("Contact", views.Contact, name='Contact')      
]