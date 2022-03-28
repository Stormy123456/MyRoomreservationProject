import base64
from django.db import models
from django.db.models import Model 

# Create your models here.

class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

class Foo(models.Model):

    _data = models.TextField(
            db_column='data',
            blank=True)
    def set_data(self, data):
        self._data = base64.encodestring(data)
    def get_data(self):
        return base64.decodestring(self._data)
    data = property(get_data, set_data)

    _data2 = models.TextField(
            db_column='emp_finger2',
            blank=True)
    def set_data(self, emp_finger2):
        self._data2 = base64.encodestring(emp_finger2)
    def get_data(self):
        return base64.decodestring(self._data)
    emp_finger2 = property(get_data, set_data)


class employee(models.Model,):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = employee.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'EMP%03d' % new_code
        super(employee, self).save(force_insert, force_update)
    emp_username=models.CharField(max_length=20,unique=True, error_messages={"unique_error_message": u"This username has already been registered."})
    emp_password=models.CharField(max_length=100)
    emp_prefix=models.CharField(max_length=10)
    emp_fname=models.CharField(max_length=50)
    emp_lname=models.CharField(max_length=50)
    emp_identification_code=models.CharField(max_length=13,unique=True)
    emp_bdate=models.DateTimeField()
    emp_image=models.ImageField(upload_to="employee_image",default="")
    status_login=models.IntegerField()

class users(models.Model):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = users.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'USR%03d' % new_code
        super(users, self).save(force_insert, force_update)
    user_username=models.CharField(max_length=20,unique=True)
    user_password=models.CharField(max_length=150)
    user_prefix=models.CharField(max_length=10)
    user_fname=models.CharField(max_length=50)
    user_lname=models.CharField(max_length=50)
    user_identification_code=models.CharField(max_length=13,unique=True)
    user_university_code=models.CharField(max_length=13,unique=True)
    user_type=models.CharField(max_length=20)
    user_bdate=models.DateTimeField()
    user_image=models.ImageField(upload_to="user_image",default="")
    user_status_finger=models.BooleanField(default=False)
    status_login=models.IntegerField()
    user_finger1 = models.CharField(max_length=150,null=True,default="")
    user_finger2 = models.CharField(max_length=150,null=True,default="")
    user_token=models.CharField(max_length=50,null=True,default="")
    user_email=models.CharField(max_length=50,null=True,default="")
    user_wrongdoing=models.IntegerField(default=0)


class reservation(models.Model):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = reservation.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'RST%03d' % new_code
        super(reservation, self).save(force_insert, force_update)
    rev_date=models.DateTimeField()
    rev_status=models.IntegerField()
    rev_num=models.CharField(max_length=20)
    rev_user=models.CharField(max_length=20)
    rev_roomid=models.CharField(max_length=20)

class roomuser(models.Model):
    rev_id = models.CharField(max_length=20)
    user = models.CharField(max_length=20)
    
class rooms(models.Model):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = rooms.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'ROM%03d' % new_code
        super(rooms, self).save(force_insert, force_update)
    rom_name=models.CharField(max_length=50,unique=True)
    rom_topic=models.CharField(max_length=20)
    rom_person=models.IntegerField()

class rounds(models.Model):
    room_id = models.CharField(max_length=20)
    room_start = models.TimeField() 
    room_stop = models.TimeField()

class idcode(models.Model):
    code = models.CharField(max_length=10)

class offender(models.Model,):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = offender.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'OFD%03d' % new_code
        super(offender, self).save(force_insert, force_update)
    ofd_punishmentstatus=models.IntegerField(default=0)
    ofd_wrongdoing=models.IntegerField(default=0)
    ofd_userid=models.CharField(max_length=20)
    ofd_day=models.DateTimeField(default='')

class banuser(models.Model,):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = banuser.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'BAN%03d' % new_code
        super(banuser, self).save(force_insert, force_update)
    ban_bdate=models.DateTimeField()
    ban_userid=models.CharField(max_length=20)
    ban_days=models.IntegerField(default=0)
    ban_punishment=models.CharField(max_length=20,default='')

class punishment(models.Model,):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = punishment.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'PNM%03d' % new_code
        super(punishment, self).save(force_insert, force_update)
    pnm_details=models.CharField(max_length=50)
    pnm_wrongdoing=models.IntegerField()
    pnm_bandays=models.IntegerField()
    pnm_status=models.CharField(max_length=20,default='0')

class roomhistorys(models.Model,):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = roomhistorys.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'HIS%03d' % new_code
        super(roomhistorys, self).save(force_insert, force_update)
    his_rev_id=models.CharField(max_length=20)
    his_rev_date=models.DateTimeField()
    his_checkin=models.TimeField()
    his_checkout=models.TimeField()

class userinroomhistorys(models.Model,):
    his_id=models.CharField(max_length=20)
    timescan=models.TimeField()
    Username=models.CharField(max_length=20)

class testhistroys(models.Model,):
    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = testhistroys.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'TES%03d' % new_code
        super(testhistroys, self).save(force_insert, force_update)
    tes_rev_id=models.CharField(max_length=20)
    tes_rev_price=models.CharField(max_length=20,default="")
    tes_rev_date=models.DateTimeField()
    tes_checkin=models.TimeField()
    tes_checkout=models.TimeField()

class testinroomhistroys(models.Model,):
    tes_id=models.CharField(max_length=20)
    testtimescan=models.TimeField()
    testusername=models.CharField(max_length=20)

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    userid=models.CharField(max_length=20)
    date=models.DateTimeField()
    time = models.TimeField()
    detail=models.CharField(max_length=50) 

class codeurl(models.Model):
    id = models.AutoField(primary_key=True)
    userid=models.CharField(max_length=20)
    code_url=models.CharField(max_length=100) 




    
   
   



