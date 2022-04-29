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
# for raw sql
from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# Create your views here.
def index(request):

    return render(request,'techcertCRUDapp/index.html')


def loginmessage(request):
    return render(request, 'techcertCRUDapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'techcertCRUDapp/logoutmessage.html')

@login_required
# pk param name must match param name in url
def person_list(request,pk):
    
    # get all instances of objects type Person & assign 
    # to person_list query set
    # assign db connection to var cursor
    cursor = connection.cursor()
    # execute SQL statement with cursor
    cursor.execute("SELECT * FROM person WHERE personkey = %s",[pk])

    # assign dict results into an array called list_of_person
    list_of_person_details = dictfetchall(cursor)

    # store details in a dict called dict_of_person_details to be rendered in context
    dict_of_person_details = list_of_person_details[0]

    # render person_list.html with context = person_list
    return render(request, 'techcertCRUDapp/person_list.html', {'person_list': dict_of_person_details})

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
            cursor = connection.cursor()

            # CREATE A (FLAG) BOOLEAN DATA STRUCTURE OR DICTIONARY TO STORE THE 3 USER LEVELS ??
            # studentstartdate, hiredate
            # studentkey, certadminkey, instructorkey
            # (student/certadmin/instructor)
            solo_keys = {'instructorkey':None,'studentkey':None,'certadminkey':None}
            group_specific_keys = {'hiredate':None, 'studentstartdate':None}
            found_solo_key = []

            # https://docs.djangoproject.com/en/4.0/ref/forms/api/#django.forms.Form.changed_data
            # store names of altered form fields in a LIST called query_field
            # TO BE TESTED: suppose the elements in the list are of the same type as the fields.
            # TO BE TESTED: changed_data[list] returns changed data accordingly to form order

            query_fields = form.changed_data

            # USE FORM.CLEANED_DATA{dictionary}, which is given after form.is_valid() == True

            # UPDATE: find out if selections are purely of type student or of type instructor and output only
            # relevant tables... depending on what fields were given, could be as direct as giving studentid or
            # instructorid or retrieval of results based on User Inputs.. easily return a queryset using vars like
            # city, lastname, firstname ... can use GTE or LTE to return a range of IDs...

            # do i check for the types of users being solicited first or do I retrieve then filter? How efficient
            # will each method do? (time complexity taken for retrieving additional rows of data compared to checking
            # subsets of data to be filtered from the start.. latter method is dependent on changed_data, which is 
            # PROBABLY smaller yet dependent on code logic)

            # iterate through changed_data to FIND
            # if (EXCLUSIVE,INDIVIDUAL) either studentkey, certadminkey, instructorkey exists:
            # store the (key-value) data; possible function instead
            def getIndividual(query_fields):
                # in operator iterates thru list..?? loop? n^2?
                if solo_keys[i] in query_fields:
                    # store key and value into new dict called found_solo_key
                    # found_solo_key[solo_keys[i]] = form.cleaned_data[solo_keys[i]]
                    found_solo_key = query_fields[i]
                
            person_exclusive_dict = {'email':None, 'phone':None}
            entity_types = ['student', 'instructor','certadmin']
            # hints that entity is a person, any user input in these categories will TECHNICALLY allow us to retrieve
            # UNIQUE entity info
            
            # SINGULAR_CASE_0 personkey, it's a key to other tables, whereas email and phones are exclusively in Person, 
            # hence needs more handling
            if 'personkey' in query_fields:
                person_key_dict['personkey'] = form.cleaned_data['personkey']

                # CASE_0_x
                # using derived key, we iterate thru possible types of entities: Student, Instructor and Certadmin 
                # and check to see which one exists and then render the data
                for i in entity_types:
                    cursor.execute("SELECT * FROM person INNER JOIN %s ON person.%s = %s.%s WHERE person.%s = %s",\
                        entity_types[i], 'personkey', entity_types[i], 'personkey', 'personkey',\
                        person_key_dict['personkey'] )
                
                    list_of_person_details = dictfetchall(cursor)

                    if list_of_person_details is not None:
                        dict_of_person_detals = list_of_person_details[0]
                        return render(request, 'techcertCRUDapp/...',{'person_profile':dict_of_person_details})

            # SINGULAR_CASE_1 check for email or phone 
            for i in person_exclusive_dict:
                if person_exclusive_dict[i] in query_fields:
                    # populate dict with user detail; consider using dict_key instead, since changed_data is just a list
                    person_exclusive_dict[i] = form.cleaned_data[form.changed_data[query_fields]]

                    # using derived key, we iterate thru possible types of entities: Student, Instructor and Certadmin 
                    # and check to see which one exists and then render the data
                    for i in entity_types:
                        cursor.execute("SELECT * FROM person INNER JOIN %s ON person.%s = %s.%s WHERE person.%s = %s",\
                            entity_types[i], person_exclusive_dict.keys(i), entity_types[i], person_exclusive_dict.keys(i), 
                            person_exclusive_dict.keys(i), person_exclusive_dict[i] )

                        # return details in a list using dictfetchall()
                        list_of_person_details = dictfetchall(cursor)


                        if list_of_person_details is not None:
                            dict_of_person_details = list_of_person_details[0]
                            return render(request, 'techcertCRUDapp/...',{'person_profile':dict_of_person_details})
            

            # SINGULAR_CASE_2 hints that entity is a student
            if found_solo_key == ['studentkey']:
                
                # COULD use dictionary unpacking to retrieve information of the single entity and store in queryset
                cursor.execute("SELECT * FROM student INNER JOIN person ON student.personid = person.personid \
                WHERE studentkey=%s",form.cleaned_data[found_solo_key])
                list_of_student_details = dictfetchall(cursor)
                dict_of_student_details = list_of_student_details[0]

                return render(request,'techcertCRUDapp/...',{'student_profile':dict_of_student_details})

            # SINGULAR_CASE_3 hints that entity is an instructor
            if found_solo_key == 'instructorkey':

                cursor.execute("SELECT * FROM instructor INNER JOIN person ON instructor.personid = person.personid \
                WHERE instructorkey=%s",form.cleaned_data[found_solo_key])

                # assign dict results into an array called list_of_student
                list_of_instructor_details = dictfetchall(cursor)

                # store details in a dict called dict_of_person_details to be rendered in context
                dict_of_instructor_details = list_of_instructor_details[0]

                return render(request,'techcertCRUDapp/...',{'instructor_profile': dict_of_instructor_details})

            # SINGULAR_CASE_4 hints that entity is a certadmin
            if found_solo_key == 'certadminkey':

                cursor.execute("SELECT * FROM certadmin INNER JOIN person ON certadmin.personid = person.personid \
                WHERE certadminkey=%s",form.cleaned_data[found_solo_key])
                list_of_certadmin_details = dictfetchall(cursor)
                dict_of_certadmin_details = list_of_certadmin_details[0]

                return render(request, 'techcertCRUDapp/...',{'certadmin_profile': dict_of_certadmin_details})

            # if not, that means it's a GROUP retrieval.. 
            # else if studentstartdate or hiredate is given,
            # construct queryset that returns results with Persons either student or instructor, 
            # along with given user inputs from Person table

            # with statuskey, or any other features, ALL THREE GROUPS are POSSIBLE, hence
            # else
            #    construct queryset that returns results with Persons that are either student, instructor or certadmin

            # HOW DO I MATCH THE USER INPUT FIELDS with their associated Table name? Model <-> Form
            # filter(instructor__hiredate='dd/mm/yy').filter(city='Seattle')
            
            ###################################################################
            #
            # straight up write the sql to retrieve list of results and render?
            # (?consequences?)
            ###################################################################
            ## solely studentstartdate and more might mean > 1 student
            ## solely hiredate and more might mean > 1 instructor
            ## studentstartdate and hiredate means both instructor and student possibilites 
            ### (? is such output ideal for school admins to have 2 or more users? Why would they do that ? how could results be 
            ###  rendered ?)
            ## any other fields might indicate all 3 users, even though certadmin is far unlikely for some fields

            # using form.cleaned_data dictionary and form.changed_data list to query sql, dictfetchall(cursor) into list and store
            # into dict to be rendered

            # if changed_data in ['postalcode','state','statuskey','lastname',firstname','address','city]
            #    create chain of filter kwargs 
            #    eg https://stackoverflow.com/questions/1227091/how-to-dynamically-provide-lookup-field-name-in-django-query?noredirect=1&lq=1
            #    eg https://stackoverflow.com/questions/310732/in-django-how-does-one-filter-a-queryset-with-dynamic-field-lookups
            person_fields = ['lastname','firstname','state','statuskey','city','postalcode']
            non_person_fields = {'student':'studentstartdate','instructor':'hiredate'}
            kwargs = {}
            for data in form.changed_data:
                if data in person_fields:
                    # add key and value into kwargs dict
                    kwargs['{0}'.format(form.cleaned_data[form.changed_data])]= form.cleaned_data[form.changed_data]
                    # remove value so 1 less check
                    person_fields.remove(data)
                    
                # if changed_data contain student field (studentstartdate)
                # lengthen filter kwargs
                if len(non_person_fields) == 2:
                    if data == non_person_fields['student']:
                        kwargs['{0}__{1}'.format('student',form.changed_data)] = form.cleaned_data[form.changed_data]
                        non_person_fields.pop('student')
                    # if changed_data contain instructor field (hiredate)
                    # lengthen filter kwargs
                    elif data  == non_person_fields['instructor']:
                        kwargs['{0}__{1}'.format('instructor', form.changed_data)] = form.cleaned_data[form.changed_data]
                        non_person_fields.pop('instructor')
            
            # query using sql or ORM and render
            return_general_query = Person.objects.filter(**kwargs)
            return render(request, 'techcertCRUDapp/...',{'general_profiles': return_general_query})


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

    # assign db connection to var cursor
    cursor = connection.cursor()
    # execute SQL statement with cursor
    cursor.execute("SELECT * FROM student WHERE studentkey = %s",[pk])

    # assign dict results into an array called list_of_student
    list_of_student_details = dictfetchall(cursor)

    # store details in a dict called dict_of_person_details to be rendered in context
    dict_of_student_details = list_of_student_details[0]

    # what url will student get after login? ie techcertCRUDapp/student=XYZ/student_profile.html
    # how would we be able to assign such URL after login?
    # can extend or inherit the same html returned by admin query POST request
    return render(request,'techcertCRUDapp/...', {'student_profile': dict_of_student_details})

# returns an atomized data of admin_query_form, but restricted to individual student and returns directly
# to the instructor upon URL request
# how would pk be gotten? from user URL?
def instructor_profile(request, pk):
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM instructor INNER JOIN person ON instructor.personkey = person.personkey \
        WHERE personkey=%s",[pk])
    # assign dict results into an array called list_of_student
    list_of_instructor_details = dictfetchall(cursor)

    # store details in a dict called dict_of_person_details to be rendered in context
    dict_of_instructor_details = list_of_instructor_details[0]

    return render(request,'techcertCRUDapp/...',{'instructor_profile': dict_of_instructor_details})

@login_required
def student_list(request,pk):

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM student INNER JOIN person ON student.personkey = person.personkey \
                WHERE studentkey=%s",[pk])

    # list called student_details that retrieves the info that is a tuple in a list
    # whereas queryset is a list of Student objects
    student_details = cursor.fetchall()
    return render(request, 'techcertCRUDapp/student_list.html', {'student_list': student_details})


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
