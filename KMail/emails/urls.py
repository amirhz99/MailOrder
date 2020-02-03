
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'emails'),
    #path('students' , views.send , name = 'email.students'),
    ]

