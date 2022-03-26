from django.contrib import admin
from .models import Person,Student,Roster

# Register your models here.
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Roster)
