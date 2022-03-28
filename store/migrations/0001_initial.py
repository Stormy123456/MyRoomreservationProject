# Generated by Django 4.0.3 on 2022-03-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banuser',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('ban_bdate', models.DateTimeField()),
                ('ban_userid', models.CharField(max_length=20)),
                ('ban_days', models.IntegerField(default=0)),
                ('ban_punishment', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='codeurl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=20)),
                ('code_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CrudUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('emp_username', models.CharField(error_messages={'unique_error_message': 'This username has already been registered.'}, max_length=20, unique=True)),
                ('emp_password', models.CharField(max_length=100)),
                ('emp_prefix', models.CharField(max_length=10)),
                ('emp_fname', models.CharField(max_length=50)),
                ('emp_lname', models.CharField(max_length=50)),
                ('emp_identification_code', models.CharField(max_length=13, unique=True)),
                ('emp_bdate', models.DateTimeField()),
                ('emp_image', models.ImageField(default='', upload_to='employee_image')),
                ('status_login', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_data', models.TextField(blank=True, db_column='data')),
                ('_data2', models.TextField(blank=True, db_column='emp_finger2')),
            ],
        ),
        migrations.CreateModel(
            name='idcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('detail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='offender',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('ofd_punishmentstatus', models.IntegerField(default=0)),
                ('ofd_wrongdoing', models.IntegerField(default=0)),
                ('ofd_userid', models.CharField(max_length=20)),
                ('ofd_day', models.DateTimeField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='punishment',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('pnm_details', models.CharField(max_length=50)),
                ('pnm_wrongdoing', models.IntegerField()),
                ('pnm_bandays', models.IntegerField()),
                ('pnm_status', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('rev_date', models.DateTimeField()),
                ('rev_status', models.IntegerField()),
                ('rev_num', models.CharField(max_length=20)),
                ('rev_user', models.CharField(max_length=20)),
                ('rev_roomid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='roomhistorys',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('his_rev_id', models.CharField(max_length=20)),
                ('his_rev_date', models.DateTimeField()),
                ('his_checkin', models.TimeField()),
                ('his_checkout', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('rom_name', models.CharField(max_length=50, unique=True)),
                ('rom_topic', models.CharField(max_length=20)),
                ('rom_person', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='roomuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_id', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='rounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=20)),
                ('room_start', models.TimeField()),
                ('room_stop', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='testhistroys',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('tes_rev_id', models.CharField(max_length=20)),
                ('tes_rev_price', models.CharField(default='', max_length=20)),
                ('tes_rev_date', models.DateTimeField()),
                ('tes_checkin', models.TimeField()),
                ('tes_checkout', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='testinroomhistroys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tes_id', models.CharField(max_length=20)),
                ('testtimescan', models.TimeField()),
                ('testusername', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='userinroomhistorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('his_id', models.CharField(max_length=20)),
                ('timescan', models.TimeField()),
                ('Username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.CharField(blank=True, default='', max_length=20, primary_key=True, serialize=False)),
                ('user_username', models.CharField(max_length=20, unique=True)),
                ('user_password', models.CharField(max_length=150)),
                ('user_prefix', models.CharField(max_length=10)),
                ('user_fname', models.CharField(max_length=50)),
                ('user_lname', models.CharField(max_length=50)),
                ('user_identification_code', models.CharField(max_length=13, unique=True)),
                ('user_university_code', models.CharField(max_length=13, unique=True)),
                ('user_type', models.CharField(max_length=20)),
                ('user_bdate', models.DateTimeField()),
                ('user_image', models.ImageField(default='', upload_to='user_image')),
                ('user_status_finger', models.BooleanField(default=False)),
                ('status_login', models.IntegerField()),
                ('user_finger1', models.CharField(default='', max_length=150, null=True)),
                ('user_finger2', models.CharField(default='', max_length=150, null=True)),
                ('user_token', models.CharField(default='', max_length=50, null=True)),
                ('user_email', models.CharField(default='', max_length=50, null=True)),
                ('user_wrongdoing', models.IntegerField(default=0)),
            ],
        ),
    ]