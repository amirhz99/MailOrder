
from django import forms
from django.core.exceptions import ValidationError
from pyad import *
import pythoncom

pyad.set_defaults(ldap_server="127.0.0.1", username="Administrator", password="12357895123Abc")

class SendStudentMailForm(forms.Form):
    First_Name = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام الزامی است'})
    Last_Name = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام خانوادگی الزامی است'})
    Student_Id = forms.IntegerField(error_messages = { 'required' : 'وارد کردن شماره دانشجویی الزامی است'})
    National_Id = forms.IntegerField(error_messages = { 'required' : 'وارد کردن کد ملی الزامی است'})
    Phone_Number = forms.IntegerField( error_messages = { 'required' : 'وارد کردن شماره همراه الزامی است'})
    College = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن دانشکده الزامی است'})
    Section = forms.CharField(max_length = 50 , error_messages = { 'required' : 'وارد کردن مقطع تحصیلی الزامی است'})
    Request_Mail = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام کاربری ایمیل در خواستی الزامی است'})
    Backup_Mail = forms.EmailField(max_length=254 , error_messages = { 'required' : 'وارد کردن ایمیل بازیابی الزامی است'})


    def clean_Request_Mail(self):


        pythoncom.CoInitialize()

        StudentId = self.cleaned_data['Student_Id']

        group = adgroup.ADGroup.from_cn("Students")
        t=0
        for user1 in group.get_members():

            if str(StudentId) in user1.get_attribute("cn"):
                t=1
        if t==0 :
            raise ValidationError('دانشجویی با این شماره دانشجویی پیدا نشد')

        RequestMail = self.cleaned_data['Request_Mail']

        for user1 in group.get_members():
            if RequestMail in user1.get_attribute("mail"):
                raise ValidationError('این ایمیل تکراری می باشد')

        return RequestMail

class SendTeacherMailForm(forms.Form):
    First_Name = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام الزامی است'})
    Last_Name = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام خانوادگی الزامی است'})
    National_Id = forms.IntegerField(error_messages = { 'required' : 'وارد کردن کد ملی الزامی است'})
    Identity_Id = forms.IntegerField(error_messages = { 'required' : 'وارد کردن شماره شناسنامه الزامی است'})
    Phone_Number = forms.IntegerField( error_messages = { 'required' : 'وارد کردن شماره همراه الزامی است'})
    College = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن دانشکده الزامی است'})
    Service = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نوع استخدام الزامی است'})
    Request_Mail = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام کاربری ایمیل در خواستی الزامی است'})
    Backup_Mail = forms.EmailField(max_length=254 , error_messages = { 'required' : 'وارد کردن ایمیل بازیابی الزامی است'})

    def clean_Request_Mail(self):

        pythoncom.CoInitialize()

        IdentityId = self.cleaned_data['Identity_Id']

        group = adgroup.ADGroup.from_cn("Teachers")
        t=0
        for user1 in group.get_members():
            if str(IdentityId) in user1.get_attribute("cn"):
                t=1
        if t==0 :
            raise ValidationError('استادی با این مشخصات پیدا نشد')

        RequestMail = self.cleaned_data['Request_Mail']

        for user1 in group.get_members():
            if RequestMail in user1.get_attribute("mail"):
                raise ValidationError('این ایمیل تکراری می باشد')

        return RequestMail



class SendEmployeeMailForm(forms.Form):
    First_Name = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام الزامی است'})
    Last_Name = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام خانوادگی الزامی است'})
    National_Id = forms.IntegerField(error_messages = { 'required' : 'وارد کردن کد ملی الزامی است'})
    Identity_Id = forms.IntegerField(error_messages = { 'required' : 'وارد کردن شماره شناسنامه الزامی است'})
    Phone_Number = forms.IntegerField( error_messages = { 'required' : 'وارد کردن شماره همراه الزامی است'})
    Service = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نوع استخدام الزامی است'})
    WorkPlace = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن محل خدمت الزامی است'})
    Assistance = forms.CharField(max_length=50 ,  error_messages = { 'required' : 'وارد کردن معاونت مربوطه الزامی است'})
    Request_Mail = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام کاربری ایمیل در خواستی الزامی است'})
    Backup_Mail = forms.EmailField(max_length=254 , error_messages = { 'required' : 'وارد کردن ایمیل بازیابی الزامی است'})

    def clean_Request_Mail(self):

        pythoncom.CoInitialize()

        IdentityId = self.cleaned_data['Identity_Id']

        group = adgroup.ADGroup.from_cn("ٍEmployees")
        t=0
        for user1 in group.get_members():
            if str(IdentityId) in user1.get_attribute("cn"):
                t=1
        if t==0 :
            raise ValidationError('کارمندی با این مشخصات پیدا نشد')
        RequestMail = self.cleaned_data['Request_Mail']

        for user1 in group.get_members():
            if RequestMail in user1.get_attribute("mail"):
                raise ValidationError('این ایمیل تکراری می باشد')

        return RequestMail

