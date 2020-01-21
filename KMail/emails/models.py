from django.db import models
from django.utils import timezone
# Create your models here.

class emails(models.Model):

    FirstName = models.CharField((""), max_length=50)
    LastName = models.CharField((""), max_length=50)
    IdNumber = models.IntegerField( )
    PhoneNumber = models.IntegerField()
    WorkPlace = models.CharField((""), max_length=50 , default = 'KHU')
    Email = models.EmailField((""), max_length=254)
    Create_at = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
 