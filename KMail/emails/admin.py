from django.contrib import admin

from .models import StudentMail,TeacherMail,EmployeeMail

admin.site.site_header = "مدیریت در خواست ایمیل"
admin.site.site_title = "پرتال در خواست ایمیل"
admin.site.index_title= "پرتال در خواست ایمیل"


@admin.register(StudentMail)
class StudentMailAdmin(admin.ModelAdmin):
    list_display = ('Last_Name' , 'Student_Id' , 'Request_Mail')

@admin.register(TeacherMail)
class TeacherMailAdmin(admin.ModelAdmin):
    list_display = ('Last_Name' , 'National_Id' , 'Request_Mail')

@admin.register(EmployeeMail)
class EmployeeMailAdmin(admin.ModelAdmin):
    list_display = ('Last_Name' , 'National_Id' , 'Request_Mail')
