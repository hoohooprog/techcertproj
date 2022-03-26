from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login',views.login, name='login'),
   path('logout',views.logout, name='logout'),
   path('person_list',views.person_list, name='person_list'),
   path('student_list',views.student_list,name='student_list'),
   path('person_form',views.person_form, name='person_form'),
]