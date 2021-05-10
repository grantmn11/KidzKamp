from django.db import models
from django.urls import reverse
from phone_field import PhoneField
# from multiselectfield import MultiSelectField
import datetime
WEEKS = (
    ('1', 'Week 1'),
    ('2', 'Week 2'),
    ('3', 'Week 3'),
    ('4', 'Week 4'),
    ('5', 'Week 5'),
    ('6', 'Week 6'),
    ('7', 'Week 7'),
    ('8', 'Week 8'),
    ('9', 'Week 9'),
    ('10', 'Week 10'),
    ('11', 'Week 11'),
)

# Create your models here.
class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneField(blank=True,E164_only=False)
    email = models.CharField(max_length=100)
    

    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse('parent_details',kwargs={'parent_id': self.id})

class Summer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    week_number = models.CharField(
        help_text='Pick Starting Week',
        max_length=12,
        choices = WEEKS,
        default = 1
        )
    phone = PhoneField(blank=True,E164_only=False)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse('summer_details', kwargs={'summer_id': self.id})

class SchoolYear(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    phone = PhoneField(blank=True,E164_only=False)
    email = models.CharField(max_length=100)

    def _str_(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse('schoolyear_details', kwargs={'school_year_id':self.id})

