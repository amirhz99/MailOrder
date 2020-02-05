
from django import forms
from django.core.exceptions import ValidationError

class SendStudentMailForm(forms.Form):
    First_Name = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام الزامی است'})
    Last_Name = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام خانوادگی الزامی است'})
    Student_Id = forms.IntegerField( error_messages = { 'required' : 'وارد کردن شماره دانشجویی الزامی است'})
    National_Id = forms.IntegerField( error_messages = { 'required' : 'وارد کردن کد ملی الزامی است'})
    Phone_Number = forms.IntegerField( error_messages = { 'required' : 'وارد کردن شماره همراه الزامی است'})
    College = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن دانشکده الزامی است'})
    Section = forms.CharField(max_length = 50 , error_messages = { 'required' : 'وارد کردن مقطع تحصیلی الزامی است'})
    Request_Mail = forms.CharField(max_length=50 , error_messages = { 'required' : 'وارد کردن نام کاربری ایمیل در خواستی الزامی است'})
    Backup_Mail = forms.EmailField(max_length=254 , error_messages = { 'required' : 'وارد کردن ایمیل بازیابی الزامی است'})


    # title.widget.attrs['class'] = 'form-control'

    # def clean_National_Id(self):
    #     NationalId = self.cleaned_data['National_Id']
    #     if len(str(NationalId)) == 10 :
    #         pass
    #     else:
    #         raise ValidationError('کد ملی باید ده رقم باشد')

    #     return NationalId
