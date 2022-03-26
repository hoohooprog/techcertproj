# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# this is an auto-generated model using inspectdb on a legacy database in pgsql
# https://docs.djangoproject.com/en/1.11/howto/legacy-databases/

# have yet to test using django database API nor admin to see data
# have yet to separate data into different apps based on the categories they are in
 
from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    attendencekey = models.AutoField(primary_key=True)
    seminardetailkey = models.ForeignKey('Seminardetails', models.DO_NOTHING, db_column='seminardetailkey')
    personkey = models.ForeignKey('Person', models.DO_NOTHING, db_column='personkey')

    class Meta:
        managed = False
        db_table = 'attendance'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Businessrule(models.Model):
    businessrulekey = models.AutoField(primary_key=True)
    businessruletext = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businessrule'


class Certadmin(models.Model):
    certadminkey = models.AutoField(primary_key=True)
    personkey = models.ForeignKey('Person', models.DO_NOTHING, db_column='personkey', blank=True, null=True)
    statuskey = models.ForeignKey('Status', models.DO_NOTHING, db_column='statuskey', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certadmin'


class Certificate(models.Model):
    certificatekey = models.AutoField(primary_key=True)
    certificatename = models.TextField()
    certificatedescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate'


class Certificatecourse(models.Model):
    certificatekey = models.OneToOneField(Certificate, models.DO_NOTHING, db_column='certificatekey', primary_key=True)
    coursekey = models.ForeignKey('Course', models.DO_NOTHING, db_column='coursekey')
    minimumgrade = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'certificatecourse'
        unique_together = (('certificatekey', 'coursekey'),)


class Course(models.Model):
    coursekey = models.AutoField(primary_key=True)
    coursename = models.TextField()
    credits = models.IntegerField()
    coursedescription = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Coursesection(models.Model):
    sectionkey = models.AutoField(primary_key=True)
    coursekey = models.ForeignKey(Course, models.DO_NOTHING, db_column='coursekey', blank=True, null=True)
    instructorkey = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='instructorkey', blank=True, null=True)
    sectionyear = models.IntegerField()
    pricehistorykey = models.ForeignKey('Pricehistory', models.DO_NOTHING, db_column='pricehistorykey', blank=True, null=True)
    quarterkey = models.ForeignKey('Quarter', models.DO_NOTHING, db_column='quarterkey', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coursesection'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Instructionalarea(models.Model):
    instructionalareakey = models.AutoField(primary_key=True)
    areaname = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructionalarea'


class Instructor(models.Model):
    instructorkey = models.AutoField(primary_key=True)
    personkey = models.ForeignKey('Person', models.DO_NOTHING, db_column='personkey', blank=True, null=True)
    hiredate = models.DateField()
    statuskey = models.ForeignKey('Status', models.DO_NOTHING, db_column='statuskey', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'


class Instructorarea(models.Model):
    instructionalareakey = models.OneToOneField(Instructionalarea, models.DO_NOTHING, db_column='instructionalareakey', primary_key=True)
    instructorkey = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='instructorkey')

    class Meta:
        managed = False
        db_table = 'instructorarea'
        unique_together = (('instructionalareakey', 'instructorkey'),)


class Location(models.Model):
    locationkey = models.IntegerField(primary_key=True)
    locationname = models.TextField()
    locationaddress = models.TextField()
    locationcity = models.TextField()
    locationstate = models.CharField(max_length=2)
    postalcode = models.CharField(max_length=12)
    phone = models.CharField(max_length=13)
    email = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Loginhistory(models.Model):
    loginhistorykey = models.AutoField(primary_key=True)
    logintablekey = models.ForeignKey('Logintable', models.DO_NOTHING, db_column='logintablekey', blank=True, null=True)
    logindate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loginhistory'


class Logintable(models.Model):
    logintablekey = models.AutoField(primary_key=True)
    username = models.TextField(blank=True, null=True)
    personkey = models.ForeignKey('Person', models.DO_NOTHING, db_column='personkey', blank=True, null=True)
    userpassword = models.TextField(blank=True, null=True)
    datelastchanged = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logintable'


class Person(models.Model):
    personkey = models.AutoField(primary_key=True)
    lastname = models.TextField()
    firstname = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    postalcode = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    dateadded = models.DateField(blank=True, null=True)
    newsletter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'
    


class Pricehistory(models.Model):
    pricehistorykey = models.AutoField(primary_key=True)
    pricebegindate = models.DateField()
    pricepercredit = models.DecimalField(max_digits=10, decimal_places=2)
    pricediscount = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pricehistory'


class Quarter(models.Model):
    quarterkey = models.AutoField(primary_key=True)
    quartername = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quarter'


class Roster(models.Model):
    rosterkey = models.AutoField(primary_key=True)
    sectionkey = models.ForeignKey(Coursesection, models.DO_NOTHING, db_column='sectionkey', blank=True, null=True)
    studentkey = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentkey', blank=True, null=True)
    finalgrade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lowgradeflag = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roster'
    
    

class Seminar(models.Model):
    seminarkey = models.AutoField(primary_key=True)
    locationkey = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationkey')
    theme = models.TextField()
    seminardate = models.DateField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seminar'


class Seminardetails(models.Model):
    topic = models.TextField()
    presenttime = models.TimeField(blank=True, null=True)
    room = models.CharField(max_length=5, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    seminardetailkey = models.AutoField(primary_key=True)
    seminarkey = models.ForeignKey(Seminar, models.DO_NOTHING, db_column='seminarkey')

    class Meta:
        managed = False
        db_table = 'seminardetails'


class Status(models.Model):
    statuskey = models.AutoField(primary_key=True)
    statusname = models.TextField()

    class Meta:
        managed = False
        db_table = 'status'


class Student(models.Model):
    studentkey = models.AutoField(primary_key=True)
    personkey = models.ForeignKey(Person, models.DO_NOTHING, db_column='personkey', blank=True, null=True)
    studentstartdate = models.DateField()
    statuskey = models.ForeignKey(Status, models.DO_NOTHING, db_column='statuskey', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

"""
unknown table, weird feature inputs, maybe it's an exercise. Also, empty.

class Substitution(models.Model):
    substitutionkey = models.AutoField(primary_key=True)
    certificatekey = models.ForeignKey(Certificate, models.DO_NOTHING, db_column='certificatekey', blank=True, null=True)
    coursekey = models.ForeignKey(Course, models.DO_NOTHING, db_column='coursekey', blank=True, null=True)
    substitutekey = models.ForeignKey(Course, models.DO_NOTHING, db_column='substitutekey', blank=True, null=True)
    studentkey = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentkey', blank=True, null=True)
    certadminkey = models.ForeignKey(Certadmin, models.DO_NOTHING, db_column='certadminkey', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'substitution'
"""