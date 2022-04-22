# https://docs.djangoproject.com/en/4.0/topics/db/queries/#making-queries
# using ORM chain filters based on altered form fields, considering spanning relationships, 
# ie joins, retrieving data using Manager into queryset

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# get models Person, Student, Roster from app's models folder
from .models import Person, Student, Roster
# get PersonForm class from app's form folder
from .forms import PersonForm, AdminQueryForm
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

# returns either form (1st pass) to same page or results from form input params 
# update-able to using serializer for encoding and transfer of data.
@login_required
def admin_person_query_ret(request):

    # check if request.method == 'POST',
        # if so, assign query form(request.POST) to variable form
        # ie binding form instance with data
    if request.method == 'POST':
        form = AdminQueryForm(request.POST)

        # if the fields are valid according to model(s) field(s) input constraints (optional/bad/required etc)
        # filters thru changed data or data that needs to be changed for POST to take effect
        if form.is_valid():
            
            # CREATE A (FLAG) BOOLEAN DATA STRUCTURE OR DICTIONARY TO STORE THE 3 USER LEVELS ??
            # studentstartdate, hiredate
            # studentkey, certadminkey, instructorkey
            # (student/certadmin/instructor)

            # https://docs.djangoproject.com/en/4.0/ref/forms/api/#django.forms.Form.changed_data
            # store names of altered form fields in a LIST called query_field
            # TO BE TESTED: suppose the elements in the list are of the same type as the fields.
            # TO BE TESTED: changed_data returns changed data accordingly to form order
            query_fields = form.changed_data

            # USE FORM.CLEANED_DATA dictionary, which is given after form.is_valid() == True

            # UPDATE: find out if selections are purely of type student or of type instructor and output only
            # relevant tables... depending on what fields were given, could be as direct as giving studentid or
            # instructorid or retrieval of results based on User Inputs.. easily return a queryset using vars like
            # city, lastname, firstname ... can use GTE or LTE to return a range of IDs...

            # do i check for the types of users being solicited first or do I retrieve then filter? How efficient
            # will each method do? (time complexity taken for retrieving additional rows of data compared to checking
            # subsets of data to be filtered from the start.. latter method is dependent on changed_data, which is 
            # PROBABLY smaller yet dependent on code logic)

            # iterate through changed_data to find
            # if (EXCLUSIVE,INDIVIDUAL) either studentkey, certadminkey, instructorkey exists:
            # store the (key-value) data
            # (except for statuskey/personkey which is general to all categories, and should be treated as such) 
            # is given,
            #    retrieve queryset based SOLELY ON keys and link back to Person and userdetails table
            # else if personkey/email/phone(?) is stated (which ALSO allows INDIVIDUAL retrieval)
            #    construct ORM-chained query(filters) based SOLELY ON personkey/email/phone(?)
            #    but need to state table derivation (ie form.cleaned_data) before stating feature name.

            # if not, that means it's a GROUP retrieval.. 
            # else if studentstartdate or hiredate is given,
            # construct queryset that returns results with Persons either student or instructor, 
            # along with given user inputs from Person table

            # with statuskey, or any other features, ALL THREE GROUPS are POSSIBLE, hence
            # else
            #    construct queryset that returns results with Persons that are either student, instructor or certadmin

            # HOW DO I MATCH THE USER INPUT FIELDS with their associated Table name? Model <-> Form
            # filter(instructor__hiredate='dd/mm/yy').filter(city='Seattle')



            # return output context to same URL? How to return same URL if its a form page prior?
            # review block tags again to see if we can insert some sort of condition? if {{ !form.isbound }} ?
            # https://stackoverflow.com/questions/12088222/calling-block-inside-an-if-condition-django-template
            # https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data#on_the_client_side_defining_how_to_send_the_data
            # https://stackoverflow.com/questions/14837312/django-taking-input-and-showing-output-in-the-same-page
            # return render(request, 'techcertCRUDapp/admin_query_form.html',{'query_results': query_results})
            pass
        else:
            form = AdminQueryForm()
            return render(request, 'admin_query_form.html',{'form':form})
    else:
        form = AdminQueryForm()
    
    return render(request, 'admin_query_form.html',{'form': form})

# returns an atomized data of admin_query_form, but restricted to individual student and returns directly
# to the student upon URL request
# how would pk be gotten? from user URL?
def student_profile(request, pk):

    student_profile = Student.objects.pk(pk)

    # what url will student get after login? ie techcertCRUDapp/student=XYZ/student_profile.html
    # how would we be able to assign such URL after login?
    # can extend or inherit the same html returned by admin query POST request
    return render(request,'techcertCRUDapp/...', {'student_profile': student_profile})

# returns an atomized data of admin_query_form, but restricted to individual student and returns directly
# to the instructor upon URL request
# how would pk be gotten? from user URL?
def instructr_profile(request, pk):

    pass

@login_required
def student_list(request):

  student_list = Student.objects.all()
  return render(request, 'techcertCRUDapp/student_list.html', {'student_list': student_list})


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
