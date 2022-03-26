
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

    return render(request,'techcertCRUDapp/index.html')


def loginmessage(request):
    return render(request, 'techcertCRUDapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'techcertCRUDapp/logoutmessage.html')

@login_required
def person_list(request):
    
    # get all instances of objects type Person & assign 
    # to person_list query set
    person_list =Person.objects.all()

    # render person_list.html with context = person_list
    return render(request, 'techcertCRUDapp/person_list.html', {'person_list': person_list})

#@login_required
#def student_list(request):

 #   student_list = Student.objects.all()
 #   return render(request, 'techcertCRUDapp/student_list.html', {'student_list': student_list})


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
    return render(request, 'techcertCRUDapp/person_form.html',{'form':form})
