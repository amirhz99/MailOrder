from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from .models import StudentMail,TeacherMail,EmployeeMail

from .form import SendStudentMailForm,SendTeacherMailForm,SendEmployeeMailForm

def index(request):
    StudentMails = StudentMail.objects.order_by('Student_Id')
    return render(request , 'index.html' ,{
        'title' : 'All StudentMails',
        'StudentMails' : StudentMails ,
    })

def students(request):

    if request.method =='POST':

        form = SendStudentMailForm(request.POST)

        if form.is_valid() :

            StudentMail.objects.create(
                First_Name = form.cleaned_data['First_Name'],
                Last_Name = form.cleaned_data['Last_Name'],
                Student_Id = form.cleaned_data['Student_Id'],
                National_Id = form.cleaned_data['National_Id'],
                Phone_Number = form.cleaned_data['Phone_Number'],
                College = form.cleaned_data['College'],
                Section = form.cleaned_data['Section'],
                Request_Mail = form.cleaned_data['Request_Mail'],
                Backup_Mail = form.cleaned_data['Backup_Mail'],
            )

            return redirect('emails:emails')

    else :
        form = SendStudentMailForm()


    return render(request , 'students.html' , { 'form' : form })

def teachers(request):

    if request.method =='POST':

        form = SendTeacherMailForm(request.POST)

        if form.is_valid() :

            TeacherMail.objects.create(
                First_Name = form.cleaned_data['First_Name'],
                Last_Name = form.cleaned_data['Last_Name'],
                National_Id = form.cleaned_data['National_Id'],
                Identity_Id = form.cleaned_data['Identity_Id'],
                Phone_Number = form.cleaned_data['Phone_Number'],
                College = form.cleaned_data['College'],
                Service = form.cleaned_data['Service'],
                Request_Mail = form.cleaned_data['Request_Mail'],
                Backup_Mail = form.cleaned_data['Backup_Mail'],
            )

            return redirect('emails:emails')

    else :
        form = SendTeacherMailForm()


    return render(request , 'teachers.html' , { 'form' : form })

def employees(request):

    if request.method =='POST':

        form = SendEmployeeMailForm(request.POST)

        if form.is_valid() :

            EmployeeMail.objects.create(
                First_Name = form.cleaned_data['First_Name'],
                Last_Name = form.cleaned_data['Last_Name'],
                National_Id = form.cleaned_data['National_Id'],
                Identity_Id = form.cleaned_data['Identity_Id'],
                Phone_Number = form.cleaned_data['Phone_Number'],
                College = form.cleaned_data['College'],
                Service = form.cleaned_data['Service'],
                WorkPlace = form.cleaned_data['WorkPlace'],
                Assistance = form.cleaned_data['Assistance'],
                Request_Mail = form.cleaned_data['Request_Mail'],
                Backup_Mail = form.cleaned_data['Backup_Mail'],
            )

            return redirect('emails:emails')

    else :
        form = SendEmployeeMailForm()


    return render(request , 'employees.html' , { 'form' : form })
