from django.contrib import admin
from .models import Parent, Summer, SchoolYear

# Register your models here.
admin.site.register(Parent)
admin.site.register(Summer)
admin.site.register(SchoolYear)