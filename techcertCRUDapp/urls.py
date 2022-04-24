# name param refers(reverses) back to this path
# https://docs.djangoproject.com/en/4.0/topics/http/urls/#reverse-resolution-of-urls
from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('loginmessage', views.loginmessage, name='loginmessage'),
   path('logoutmessage',views.logoutmessage, name='logoutmessage'),
   # pk name must be same as fn header's name
   path('person_list/person/<int:pk>/',views.person_list, name='person_list'),
   path('student_list',views.student_list,name='student_list'),
   path('person_form',views.person_form, name='person_form'),
   # url route for html page called 'admin_query_form' to view of form, set internal name as 'admin_query_form'
   path('admin_query_form',views.admin_person_query_ret, name='admin_query_form')
   # url route to login unique students?
]