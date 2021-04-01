from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('photos/', views.photos, name='photos'),
    # path('parent/', views.parent, name = 'parent'),
    path('parent/', views.parent_index, name='parent_index'),
    path('parent/<int:parent_id>/', views.parent_details, name = 'parent_details'),
    path('parent/create', views.CreateParent.as_view(), name= 'parent_create'),
    path('program/afterschool', views.afterschool, name='afterschool'),
    path('program/summer', views.summer, name='summer'),
   
    
]