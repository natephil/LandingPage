from django.db import models

# Create your models here.
class newLead(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    address_of_property = models.CharField(max_length=250)
    def __str__(self):
        return self.last_name
    class Meta:
        ordering = ['last_name']
    class Admin:
        pass