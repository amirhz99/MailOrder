
from django import forms
from django.core.exceptions import ValidationError
#import unicodecsv as csv
#import active_directory

# import python-ldap

# l = ldap.open("192.168.159.133")

	# you should  set this to ldap.VERSION2 if you're using a v2 directory
# l.protocol_version = ldap.VERSION3
	# Pass in a valid username and password to get
	# privileged directory access.
	# If you leave them as empty strings or pass an invalid value
	# you will still bind to the server but with limited privileges.

# username = "cn=Administrator, o=com.ghdam.root"
# password  = "12357895123Abc"

	# Any errors will throw an ldap.LDAPError exception
	# or related exception so you can ignore the result
# l.simple_bind(username, password)
	# handle error however you like
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


    # homeMDB = "CN=UBER MAILBOX,CN=InformationStore,CN=UBERMAILSERVER,"\
    #         "CN=Servers,CN=Administrative Groups,CN=UBERORG,"\
    #         "CN=Microsoft Exchange,CN=Services,CN=Configuration,"\
    #         "DC=uber,DC=org,DC=uk"

    # user=active_directory.find_user("captain.awesomeface")
    # user.CreateMailbox(homeMDB)


    # user.Properties["mail"].Value = "captain.awesomeface@uberorg.com";

    # user.SetInfo()

    # with open('chargoon.csv','rb') as csvfile:
    #         reader = csv.reader(csvfile)
    #             for row in reader:

    def clean_Request_Mail(self):

        RequestMail = self.cleaned_data['Request_Mail']

        if RequestMail == 'zarei.100' :
            raise ValidationError('این نام کاربری تکراری می باشد')

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
