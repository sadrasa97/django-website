from django.contrib import admin
from django.urls import path,include
from blog.views import *
app_name='blog'
urlpatterns = [
    path('',blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    #path('<str:name>/<str:family_name>/<int:age>',test,name='test')
    
]