from django.db import models
from django.urls import reverse
from phone_field import PhoneField



# Create your models here.
class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact Phone Number',E164_only=False)
    email = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('parent_details',kwargs={'parent_id': self.id})



