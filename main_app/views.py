from django.shortcuts import render, redirect

from .models import Parent
from django.views.generic.edit import CreateView


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

def parent_index(request):
    parents = Parent.objects.all()
    
    return render(request, 'parents/index.html', {'parents': parents})


def parent_details(request, parent_id):
    parent = Parent.objects.get(id=parent_id)
    return render(request, 'parents/details.html',{'parent': parent})


# def parent_details(request, parent_id):
#     parent = Parent.objects.get(id=parent_id)
#     parent_form = ParentForm()
#     return render(redirect, 'parent_details',{'parent':parent, 'parent_form':parent_form})
class CreateParent(CreateView):
  model = Parent
  fields = ['first_name', 'last_name','phone','email']
  




  


# def add_child(request, parent_id):
#   form = ChildForm(request.POST)
#   if form.is_valid():
#     new_comment = form.save(commit=False)
#     new_comment.parent_id = parent_id
#     # new_comment.update('content')
#     new_comment.save()
#   return redirect('parent_details', parent_id = parent_id)



# def add_parent(request, parent_id):
#     form = ParentForm(request.POST)
#     if form.is_valid():
#         new_parent = form.save(commit=False)
#         new_parent.parent_id = parent_id
#         new_parent.save()
#     return redirect('parent_index', parent_id=parent_id)