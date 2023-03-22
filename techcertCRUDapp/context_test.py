from django.db import connection
from django.template import Context, Template
from .models import Person

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
	
"""
cursor = connection.cursor()
cursor.execute("SELECT * FROM person WHERE personkey = %s",[276])
person_list = dictfetchall(cursor)
print(person_list)
t = Template("My name is {{student.lastname}}")

t.render(Context({'student':person_list}))
"""

""" context tutorial """
# tutorial03: "the context is a dictionary mapping template variable names
#	     to Python objects"

# django.template.Context
# https://docs.djangoproject.com/en/2.2/_modules/django/template/context/

"""
for simple use, class Context takes an optional arg - a dict mapping variable
names to variable values/Python objects
{{ foo.bar }} will be interpreted as a literal string and not use the value
of the variable
MEANING: if there's a variable named foo.bar in context, it will be ignored
eg if d = {"person.first_name":{"first_name":"Joe"},"person":{"first_name":"Isaac"}} 
 then d["person.first_name"]will be ignored

foo.bar will not be seen as a variable but a string that requires further processing and
for lookups to be performed. 

Dots have a special meaning in template rendering.
A dot in a variable name signifies a lookup. 
Specifically, when the template system encounters a dot in a variable name,
it tries the following lookups, in this order:
1) Dictionary lookup. Eg: foo["bar"]
2) Attribute lookup. Eg: foo.bar
3) List-index lookup. Eg: foo[bar}

if class -> d.get('person'),p.last_name ~~ person_obj = d.get('person'); person_obj.last_name;
if array -> dict_stooges.get('stooges')[0] ~~ arr = dict_stooges.get('stooges'); arr[0];
if dict -> d.get('person')['first_name'] ~~ person = d.get('person'); person['first_name'];
"""























