from django.db import models
from django.utils import timezone

class StudentMail(models.Model):

    First_Name = models.CharField(max_length=50 , verbose_name = "نام")
    Last_Name = models.CharField(max_length=50, verbose_name = " نام خانوادگی")
    Student_Id = models.IntegerField(verbose_name = "شماره دانشجویی")
    National_Id = models.IntegerField(verbose_name = "کد ملی" )
    Phone_Number = models.IntegerField(verbose_name = "شماره همراه")
    College = models.CharField(max_length=50 , default = 'KHU', verbose_name = "دانشکده")
    Section = models.CharField(max_length = 50, verbose_name = "مقطع تحصیلی")
    Request_Mail = models.CharField(max_length=50, verbose_name = "ایمیل در خواستی")
    Backup_Mail = models.EmailField(max_length=254, verbose_name = "ایمیل پشنیبانی")

    class Meta:
        verbose_name = ("ایمبل دانشجویان")
        verbose_name_plural = ("ایمبل های دانشجویان")

    def __str__(self):
        return self.Request_Mail

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class TeacherMail(models.Model):

    First_Name = models.CharField(max_length=50 , verbose_name = "نام")
    Last_Name = models.CharField(max_length=50 , verbose_name = " نام خانوادگی")
    National_Id = models.IntegerField(verbose_name = "کد ملی")
    Identity_Id = models.IntegerField(verbose_name = "شماره شناسنامه")
    Phone_Number = models.IntegerField(verbose_name = "شماره همراه")
    College = models.CharField(max_length=50 , default = 'KHU', verbose_name = "دانشکده محل تدریس")
    Service = models.CharField(max_length=50 , verbose_name = "نوع استخدام")
    Request_Mail = models.CharField(max_length=50 , verbose_name = "ایمیل در خواستی")
    Backup_Mail = models.EmailField(max_length=254 , verbose_name = "ایمیل پشنیبانی")

    class Meta:
        verbose_name = ("ایمیل اساتید")
        verbose_name_plural = ("ایمیل های اساتید")

    def __str__(self):
        return self.Request_Mail

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class EmployeeMail(models.Model):

    First_Name = models.CharField(max_length=50 , verbose_name = "نام")
    Last_Name = models.CharField(max_length=50 , verbose_name = " نام خانوادگی")
    National_Id = models.IntegerField(verbose_name = "کد ملی")
    Identity_Id = models.IntegerField(verbose_name = "شماره شناسنامه" )
    Phone_Number = models.IntegerField(verbose_name = "شماره همراه")
    College = models.CharField(max_length=50 , default = 'KHU' , verbose_name = "دانشکده")
    Service = models.CharField(max_length=50 , verbose_name = "نوع استخدام")
    WorkPlace = models.CharField(max_length=50 , verbose_name = "محل خدمت")
    Assistance = models.CharField(max_length=50 ,  verbose_name = "ذیل کدام معاونت فعالیت می کنید")
    Request_Mail = models.CharField(max_length=50 , verbose_name = "ایمیل در خواستی")
    Backup_Mail = models.EmailField(max_length=254, verbose_name = "ایمیل پشنیبانی")

    class Meta:
        verbose_name = ("ایمیل کارمندان")
        verbose_name_plural = ("ایمیل های کارمندان")

    def __str__(self):
        return self.Request_Mail

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})