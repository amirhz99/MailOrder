
from django.urls import path
from . import views

app_name = 'emails'
urlpatterns = [
    path('', views.index , name = 'emails'),
    path('students' , views.students , name = 'email.students'),
    path('teachers' , views.teachers, name = 'email.teachers'),
    path('employees' , views.employees , name = 'email.employees'),
    ]

