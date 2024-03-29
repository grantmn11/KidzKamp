from django.shortcuts import render, redirect

from .models import Parent, Summer, SchoolYear
from django.views.generic.edit import CreateView
# from multiselectfield import MultiSelectField


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def photos(request):
    return render(request,'photos.html')

def summer(request):
    return render(request,'program/summer.html')

def afterschool(request):
    return render(request,'program/afterschool.html')

# def parent(request):
#     return render(request, 'parent.html')
def school_year(request):
    school_year = SchoolYear.objects.all()

    return render(request, 'program/afterschool.html', {'school_year': school_year})

def schoolyear_details(request,school_year_id):
    school_year = SchoolYear.objects.get(id=school_year_id)
    return render(request, 'schoolyear/details.html', { 'school_year': school_year})


def parent_index(request):
    parents = Parent.objects.all()
    
    return render(request, 'parents/index.html', {'parents': parents})


def parent_details(request, parent_id):
    parent = Parent.objects.get(id=parent_id)
    return render(request, 'parents/details.html',{'parent': parent})

def summer_index(request):
    summer = Summer.objects.all()

    return render(request, 'summer/index.html',{'summer': summer})

def summer_details(request, summer_id):
    summer = Summer.objects.get(id=summer_id)
    return render(request, 'summer/details.html', {'summer': summer})



# def parent_details(request, parent_id):
#     parent = Parent.objects.get(id=parent_id)
#     parent_form = ParentForm()
#     return render(redirect, 'parent_details',{'parent':parent, 'parent_form':parent_form})
class CreateParent(CreateView):
  model = Parent
  fields = ['first_name', 'last_name','phone','email']
  

class CreateSummer(CreateView):
    model = Summer
    fields = ['first_name', 'last_name', 'child_name', 'week_number', 'email', 'phone']

class CreateSchoolYear(CreateView):
    model = SchoolYear
    fields = ['first_name', 'last_name', 'child_name', 'phone', 'email']
