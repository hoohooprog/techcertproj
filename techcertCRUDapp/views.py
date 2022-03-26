
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# get models Person, Student, Roster from app's models folder
from .models import Person, Student, Roster
# get PersonForm class from app's form folder
from .forms import PersonForm
# include for login_auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request,'index.html')


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

@login_required
def person_list(request):
    return render(request, 'person_list.html')

@login_required
def student_list(request):
    return render(request, 'student_list.html')


# decorator
@login_required
# Create a form to add a resource and a form to add a meeting (A8)
def person_form(request):
    form = PersonForm
    if request.method == 'POST':
        form=PersonForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            # make a new form
            form=PersonForm()
    else:
        form=PersonForm()
    return render(request, 'nperson_form.html',{'form':form})
