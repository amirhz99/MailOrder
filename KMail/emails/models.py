from django.db import models
from django.utils import timezone
# Create your models here.

class email(models.Model):

    First_Name = models.CharField((""), max_length=50)
    Last_Name = models.CharField((""), max_length=50)
    Id_Number = models.IntegerField( )
    Phone_Number = models.IntegerField()
    WorkPlace = models.CharField((""), max_length=50 , default = 'KHU')
    Email = models.EmailField((""), max_length=254)
    Create_at = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.Email

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
