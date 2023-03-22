from socket import fromshare
from django import forms
from .models import Person


# class inherits forms.ModelForm
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

ENTITY_TYPE_CHOICES = ['Student','Instructor','CertAdmin']
# a (query) Form class that accepts inputs based on person table but can withdraw
# information from other tables such as logintable(username, userpassword, datelastchanged)
# and its related table loginhistory
# student(studentstartdate,status(key)) or instructor (hiredate, status(key)) and instructor's
# corresponding instructionalarea

# It is a form that admin has unrestricted access to person info or information based
# on combinations of input features of forms. fields that admin would normally insert to query are:
#

## ?? how about an add field form such that form is unrestricted and expands depending on search criteria ?? 
## (smallest set)
## general: returns person info(person) + login info (logintable+loginhistory)

## (super set 1)
## instructor returns: general + instructor info(instructor+instructorarea+instructionalarea+status) + 
## course info(course+coursesection+quarter)

## (super set 2)
## student returns: general + student info(student+roster) + course info(course+coursesection+quarter) + 
## certificate info(certificate+certificatecourse)

## (super set 3) 
## certadmin (optional for now)

## only key type that is output is personkey and sectionkey (for students, since it's self-representive)
## provides general person info, along with login info, type of person and status
class AdminQueryForm(forms.Form):

    # 1. drop down field that allows 3 (optional) selection: student or instructor or certadmin
    entity_type = ChoiceField(label='person category', choices= ENTITY_TYPE_CHOICES)
    # 2. lastname (optional)
    lastname = CharField(label='last name')
    # 3. firstname (optional)
    firstname = Charfield(label='first name')
    # 4. email (optional)
    email = EmailField(label='email address')
    # 5. address (optional)
    address = CharField(label='address')
    # 6. city (optional)
    city = CharField(label='city')
    # 7. state (optional)
    state = CharField(label='state')
    # 8. postalcode (optional)
    postalcode = IntegerField(label='postal code')
    # 9. phone (optional)
    phone = IntegerField(label='phone')
    # 10. dateadded (optional)
    dateadded = DateField(label = 'date added')
    

# if is-a student, show info on current and past classes and cert type, links to person info or course/class info
class AdminStudentQueryInfoForm(forms.Form):
    pass

class AdminClassQueryForm(forms.Form):
    pass

## sub-class of AdminQueryForm? what can students retrieve?
## sub-class of AdminQueryForm; retrieving only 
class StudentCourseQueryForm(forms.Form):
    pass

## what can instructors retrieve/view??
class InstructorQueryForm(forms.Form):
    pass
# query form that allows Users to retrieve their login info

# update form that allows Users to change their password