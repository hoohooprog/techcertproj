from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('loginmessage', views.loginmessage, name='loginmessage'),
   path('logoutmessage',views.logoutmessage, name='logoutmessage'),
   path('person_list',views.person_list, name='person_list'),
   #path('student_list',views.student_list,name='student_list'),
   path('person_form',views.person_form, name='person_form'),
]