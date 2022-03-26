from django.test import TestCase


from .models import Person
from .forms import PersonForm
from django.db import models
from django.urls import reverse

# Create your tests here.
class PersonTest(TestCase):

    
    def setup(self):
        
        personTest = Person(personkey=100, lastname='Tay', firstname='J', email='tjingyi@ucsd.edu',address='814 Nunc Street', 
                city='Las Vegas',state='NV', postalcode='89101',phone='(703)275-1784',dateadded='2021-01-22',newsletter='true')
        return personTest

    def test_table(self):
        stud = self.setup()
        
        self.assertEqual(str(Person._meta.db_table),'person')

    def test_personKey(self):
        stud = self.setup()

        self.assertEqual(stud.personkey, 100)

    def test_lastname(self):
        stud = self.setup()
        self.assertEqual(stud.lastname,'Tay')

    def test_firstname(self):
        stud = self.setup()
        self.assertEqual(stud.firstname,'J')
    
    def test_email(self):
        stud = self.setup()
        self.assertEqual(stud.email,'tjingyi@ucsd.edu')

    def test_address(self):
        stud = self.setup()
        self.assertEqual(stud.address,'814 Nunc Street')

    def test_city(self):
        stud = self.setup()
        self.assertEqual(stud.city,'Las Vegas')

    def test_state(self):
        stud = self.setup()
        self.assertEqual(stud.state,'NV')

    def test_postalcode(self):
        stud = self.setup()
        self.assertEqual(stud.postalcode,'89101')

    def test_phone(self):
        stud = self.setup()
        self.assertEqual(stud.phone,'(703)275-1784')

    def test_dateadded(self):
        stud = self.setup()
        
        self.assertEqual(stud.dateadded, '2021-01-22')

    def test_newsletter(self):
        stud = self.setup()
        self.assertEqual(stud.newsletter, 'true')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


# https://stackoverflow.com/questions/30897442/django-1-8-fails-to-django-db-utils-programmingerror-relation-auth-user-does
class PersonForm_Test(TestCase):
    def test_form_is_valid(self):
        form=PersonForm(data={'lastname': "tay", 'firstname':"J",'email':"tjingyi@ucsd.edu",'address':"capitol hill", 'city':"seattle",'state':"WA",'postalcode':"98122",
                'phone':"(703)275-1784",'dateadded':"2021-01-22",'newsletter':"true"})
        self.assertTrue(form.is_valid())
        