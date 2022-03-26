# Generated by Django 4.0.1 on 2022-03-26 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendencekey', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'attendance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Businessrule',
            fields=[
                ('businessrulekey', models.AutoField(primary_key=True, serialize=False)),
                ('businessruletext', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'businessrule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Certadmin',
            fields=[
                ('certadminkey', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'certadmin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('certificatekey', models.AutoField(primary_key=True, serialize=False)),
                ('certificatename', models.TextField()),
                ('certificatedescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'certificate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('coursekey', models.AutoField(primary_key=True, serialize=False)),
                ('coursename', models.TextField()),
                ('credits', models.IntegerField()),
                ('coursedescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coursesection',
            fields=[
                ('sectionkey', models.AutoField(primary_key=True, serialize=False)),
                ('sectionyear', models.IntegerField()),
            ],
            options={
                'db_table': 'coursesection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instructionalarea',
            fields=[
                ('instructionalareakey', models.AutoField(primary_key=True, serialize=False)),
                ('areaname', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'instructionalarea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructorkey', models.AutoField(primary_key=True, serialize=False)),
                ('hiredate', models.DateField()),
            ],
            options={
                'db_table': 'instructor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationkey', models.IntegerField(primary_key=True, serialize=False)),
                ('locationname', models.TextField()),
                ('locationaddress', models.TextField()),
                ('locationcity', models.TextField()),
                ('locationstate', models.CharField(max_length=2)),
                ('postalcode', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loginhistory',
            fields=[
                ('loginhistorykey', models.AutoField(primary_key=True, serialize=False)),
                ('logindate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'loginhistory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logintable',
            fields=[
                ('logintablekey', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField(blank=True, null=True)),
                ('userpassword', models.TextField(blank=True, null=True)),
                ('datelastchanged', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'logintable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('personkey', models.AutoField(primary_key=True, serialize=False)),
                ('lastname', models.TextField()),
                ('firstname', models.TextField(blank=True, null=True)),
                ('email', models.TextField(unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('postalcode', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
                ('dateadded', models.DateField(blank=True, null=True)),
                ('newsletter', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pricehistory',
            fields=[
                ('pricehistorykey', models.AutoField(primary_key=True, serialize=False)),
                ('pricebegindate', models.DateField()),
                ('pricepercredit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pricediscount', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'pricehistory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('quarterkey', models.AutoField(primary_key=True, serialize=False)),
                ('quartername', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'quarter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('rosterkey', models.AutoField(primary_key=True, serialize=False)),
                ('finalgrade', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('lowgradeflag', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'roster',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('seminarkey', models.AutoField(primary_key=True, serialize=False)),
                ('theme', models.TextField()),
                ('seminardate', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'seminar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seminardetails',
            fields=[
                ('topic', models.TextField()),
                ('presenttime', models.TimeField(blank=True, null=True)),
                ('room', models.CharField(blank=True, max_length=5, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('seminardetailkey', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'seminardetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('statuskey', models.AutoField(primary_key=True, serialize=False)),
                ('statusname', models.TextField()),
            ],
            options={
                'db_table': 'status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentkey', models.AutoField(primary_key=True, serialize=False)),
                ('studentstartdate', models.DateField()),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Certificatecourse',
            fields=[
                ('certificatekey', models.OneToOneField(db_column='certificatekey', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='techcertCRUDapp.certificate')),
                ('minimumgrade', models.DecimalField(decimal_places=65535, max_digits=65535)),
            ],
            options={
                'db_table': 'certificatecourse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instructorarea',
            fields=[
                ('instructionalareakey', models.OneToOneField(db_column='instructionalareakey', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='techcertCRUDapp.instructionalarea')),
            ],
            options={
                'db_table': 'instructorarea',
                'managed': False,
            },
        ),
    ]
