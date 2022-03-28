from django.db.models.fields import DateField
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from.models import Log, employee, idcode,users,reservation,rooms,rounds,roomuser,CrudUser,banuser,roomhistorys,userinroomhistorys,offender,banuser,punishment,testhistroys,testinroomhistroys
from datetime import datetime
from .utils import get_plot
from django.db import connection 
from django.db import connections
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django_file_md5 import calculate_md5
from django.contrib.auth.hashers import make_password
from operator import itemgetter
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.template.loader import render_to_string
from django import forms
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime, timedelta
from django.db import connection
from django.shortcuts import get_object_or_404
from datetime import date
from datetime import datetime
from datetime import datetime, timedelta
from datetime import date, datetime
from django.db.models.functions import Lower
from django.db.models.functions import Reverse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile
# from tasks.forms import TaskForm
# from tasks.models import Task
from django.views import View
from datetime import date
from datetime import datetime
from django.utils import timezone
from datetime import date, datetime
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import datetime
from datetime import datetime
from datetime import datetime, date, timedelta

import time
import datetime
import json
import mysql.connector

import sys
import hashlib
import os
from pprint import pprint
import urllib
import json
import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from pprint import pprint
from urllib.request import Request, urlopen
from django.views.generic import ListView
from django.views.generic import View
from .forms import BookForm
from .forms import ProductForm
from .forms import RoomhistoryForm

from datetime import date, timedelta
from django.http import JsonResponse
import json


# Create your views here.
def save_Roomhistory_form(request, form, his_id, template_name):
    data = dict()
    user = request.session.get('id_user')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = roomhistorys.objects.all()
            data['html_product_list'] = render_to_string('includes/historyusingroom_list.html', {
                'products': products
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def roomhistoryviews(request, pk):
    his_id = pk
    product2 = get_object_or_404(userinroomhistorys, his_id=pk)
    # product2 = userinroomhistorys.objects.filter(his_id=pk)
    if request.method == 'POST':
        form = RoomhistoryForm(request.POST, instance=product2)

    else:
        form = RoomhistoryForm(instance=product2)

    return save_Roomhistory_form(request, form , his_id, 'includes/viewhistory.html')


def product_list(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            user = request.session.get('id_user')
            products = users.objects.filter(user_username=user)
            user_username = request.session.get('id_user')
            image = userimagedata(user_username)
            return render(request, 'product_list.html', {'products': products,'image':image})
        else:
            return redirect("/")

def save_product_form(request, form, template_name):
    data = dict()
    user = request.session.get('id_user')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = users.objects.filter(user_username=user)
            data['html_product_list'] = render_to_string('includes/partial_product_list.html', {
                'products': products
            })
            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'edit user profile'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()
    return save_product_form(request, form, 'includes/partial_product_create.html')

def product_update(request, pk):
    product = get_object_or_404(users, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
    else:
        form = ProductForm(instance=product)
    return save_product_form(request, form, 'includes/partial_product_update.html')

def product_delete(request, pk):
    product = get_object_or_404(users, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.delete()
        data['form_is_valid'] = True
        products = CrudUser.objects.all()
        data['html_product_list'] = render_to_string('includes/partial_product_list.html', {
            'products': products
        })
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('includes/partial_product_delete.html', context, request=request)
    return JsonResponse(data)

def book_list(request):
	books = CrudUser.objects.all()
	context = {
	'books': books
	}
	return render(request, 'book_list.html',context)

def book_create(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
	else:
		form = BookForm()
	return save_all(request,form,'book_create.html')

class CrudView(ListView):
    model = employee
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'

class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = employee.objects.get(id=id1)
        obj.emp_prefix = name1
        obj.emp_fname = address1
        obj.emp_lname = age1
        obj.save()

        user = {'id':obj.id,'name':obj.emp_prefix,'address':obj.emp_fname,'age':obj.emp_lname}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def imagedata(emp_username):
    imgdata = employee.objects.filter(emp_username=emp_username)
    return imgdata

def userimagedata(user_username):
    imgdata = users.objects.filter(user_username=user_username)
    return imgdata

def index(request):
    x = request.session.get('logged_in')
    emp_username = request.session.get('id_user')  
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            image = imagedata(emp_username)
            empdata = employee.objects.filter(emp_username=emp_username)
            return render(request,'index.html',{'empdata':empdata,'image':image})
        else:
            return redirect("/")

def historyBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            x = []
            chart = get_plot(x)
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'historyBoard.html',{'chart':chart,'image':image})
        else:
            return redirect("/")

def historyReservation(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            reserve = reservation.objects.all()
            round = rounds.objects.all()
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'historyReservation.html',{'image':image,'reserve':reserve,'round':round})
        else:
            return redirect("/")

def historySearch(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            alltime = request.POST['alltime']
            start = request.POST['start']
            stop = request.POST['stop']
            checkalltime = str(alltime)
            if(checkalltime == "0"):
                if(start == '' or stop ==''):
                    messages.success(request, 'กรุณาเลือกช่วงเวลาที่ต้องการค้นหา')
                    x = []
                    chart = get_plot(x)
                    findemp_username = request.session.get('id_user')  
                    image2 = imagedata(findemp_username)
                    return render(request,'historyBoard.html',{'chart':chart,'image':image2})
                else:
                    hisdata = roomhistorys.objects.filter(his_rev_date__gte=start).filter(his_rev_date__lte=stop)
                    if(hisdata):
                        x = [x.his_rev_id for x in hisdata]
                        chart = get_plot(x)
                        emp_username = request.session.get('id_user')  
                        image = imagedata(emp_username)
                        return render(request,'historyBoard.html',{'chart':chart,'image':image})
                    else:
                        messages.success(request, 'ไม่พบประวัติการใช้งานใดๆ ในช่วงเวลาที่ท่านเลือก')
                        x = []
                        chart = get_plot(x)
                        emp_username = request.session.get('id_user')  
                        image = imagedata(emp_username)
                        return render(request,'historyBoard.html',{'chart':chart,'image':image})
            else:
                hisdata = roomhistorys.objects.all()
                x = [x.his_rev_id for x in hisdata]
                chart = get_plot(x)

                userid = request.session.get('id')
                date = datetime.date.today()
                time = datetime.datetime.now()
                detail = 'rescarch history using room'
                logging = Log(userid=userid,date=date,time=time,detail=detail)
                logging.save()
                emp_username = request.session.get('id_user')  
                image = imagedata(emp_username)
                return render(request,'historyBoard.html',{'chart':chart,'image':image})
        else:
            return redirect("/")

def punishmentBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            punishmentdata = punishment.objects.all()
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'punishmentBoard.html',{'punishmentdata':punishmentdata,'image':image})
        else:
            return redirect("/")

def punishmentAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'punishmentAdd.html',{'image':image})
        else:
            return redirect("/")

def punishmentAddnewdata(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/") 
    else:
        if (x == 1):
            pnm_details = request.POST['pnm_details']
            pnm_wrongdoing = request.POST['pnm_wrongdoing']
            pnm_bandays = request.POST['pnm_bandays']
            content = punishment(pnm_details=pnm_details,pnm_wrongdoing=pnm_wrongdoing,pnm_bandays=pnm_bandays)
            checkwrongdoing = int(pnm_wrongdoing)
            if(checkwrongdoing!=0):
                if(punishment.objects.filter(pnm_wrongdoing=pnm_wrongdoing)):
                    messages.success(request, 'จำนวนครั้งในการทำผิดนี้ มีบทลงโทษอยู่แล้ว')
                    return redirect("/punishmentAdd")
                else:
                    content.save()

                    userid = request.session.get('id')
                    date = datetime.date.today()
                    time = datetime.datetime.now()
                    detail = 'add punishment data'
                    logging = Log(userid=userid,date=date,time=time,detail=detail)
                    logging.save()

                    messages.success(request, 'เพิ่มบทลงโทษสำเร็จ')
                    return redirect("/punishmentBoard")
            else:
                content.save()
                userid = request.session.get('id')
                date = datetime.date.today()
                time = datetime.datetime.now()
                detail = 'add punishment data'
                logging = Log(userid=userid,date=date,time=time,detail=detail)
                logging.save()
                messages.success(request, 'เพิ่มบทลงโทษสำเร็จ')
                return redirect("/punishmentBoard")
        else:
            return redirect("/")

def punishmentToggleOff(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            content = punishment.objects.get(pk = id)
            content.pnm_status = 1
            content.save()
            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'switch Off punishment data'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()
            punishmentdata = punishment.objects.all()
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'punishmentBoard.html',{'punishmentdata':punishmentdata,'image':image})
            # return redirect("/punishmentBoard")
        else:
            return redirect("/")

def punishmentToggleOn(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            content = punishment.objects.get(pk = id)
            content.pnm_status = 0
            content.save()
            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'switch On punishment data'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()
            punishmentdata = punishment.objects.all()
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'punishmentBoard.html',{'punishmentdata':punishmentdata,'image':image})
            # return redirect("/punishmentBoard")
        else:
            return redirect("/")

def punishmentEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = punishment.objects.filter(pk=id)
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'punishmentEdit.html',{'result':result,'image':image})
        else:
            return redirect("/")

def punishmentUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id']
                olddata = punishment.objects.get(pk=id)
                oldwrongdoing = olddata.pnm_wrongdoing

                content = punishment.objects.get(pk=id)
                content.pnm_wrongdoing = 0
                content.save()
                
                pnm_details = request.POST['pnm_details']
                pnm_wrongdoing = request.POST['pnm_wrongdoing']
                pnm_bandays = request.POST['pnm_bandays']
                content = punishment.objects.get(id=id)
                content.pnm_details = pnm_details
                content.pnm_wrongdoing = pnm_wrongdoing
                content.pnm_bandays = pnm_bandays
                result = punishment.objects.filter(pk=id)
                checkwrongdoing = int(pnm_wrongdoing)
                if(checkwrongdoing!=0):
                    if(punishment.objects.filter(pnm_wrongdoing=pnm_wrongdoing)):
                        content = punishment.objects.get(pk = id)
                        content.pnm_wrongdoing = oldwrongdoing
                        content.save()
                        messages.success(request, 'จำนวนครั้งในการทำผิดนี้ มีบทลงโทษอยู่แล้ว')
                        emp_username = request.session.get('id_user')  
                        image = imagedata(emp_username)
                        return render(request,'punishmentEdit.html',{'result':result,'image':image})
                    else:
                        content.save()

                        userid = request.session.get('id')
                        date = datetime.date.today()
                        time = datetime.datetime.now()
                        detail = 'edit punishment data'
                        logging = Log(userid=userid,date=date,time=time,detail=detail)
                        logging.save()

                        messages.success(request, 'แก้ไขบทลงโทษสำเร็จ')
                        return redirect("/punishmentBoard")
                else:
                    content.save()

                    userid = request.session.get('id')
                    date = datetime.date.today()
                    time = datetime.datetime.now()
                    detail = 'edit punishment data'
                    logging = Log(userid=userid,date=date,time=time,detail=detail)
                    logging.save()

                    messages.success(request, 'แก้ไขบทลงโทษสำเร็จ')
                    return redirect("/punishmentBoard")

            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

def punishmentDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            punishment.objects.filter(id=id).delete()
            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'delete punishment data'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()
            return redirect("/punishmentBoard")
        else:
            return redirect("/")

def banuserBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            bandata = banuser.objects.all()
            punishmentdata = punishment.objects.filter(Q(pnm_wrongdoing=0), Q(pnm_status='0'))
            usersdata = users.objects.all()
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'banuserBoard.html',{'image':image,'punishmentdata':punishmentdata,'bandata':bandata,'usersdata':usersdata})
        else:
            return redirect("/")

def banuserAddnewdata(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/") 
    else:
        if (x == 1):
            today = datetime.date.today()
            ban_userid = request.POST['ban_userid']
            ban_punishment = request.POST['ban_punishment']
            ban_bdate = today
            mypunishmentdata = punishment.objects.filter(id = ban_punishment)
            for data in mypunishmentdata:
                ban_days = data.pnm_bandays
            content = banuser(ban_userid=ban_userid,ban_punishment=ban_punishment,ban_bdate=ban_bdate,ban_days=ban_days)
    
            if(banuser.objects.filter(ban_userid=ban_userid)):
                messages.success(request, 'ผู้ใช้นี้อยู่ระหว่างการแบนอยู่แล้ว')
                return redirect("/banuserBoard")
            else:
                content.save()
                userid = request.session.get('id')
                date = datetime.date.today()
                time = datetime.datetime.now()
                detail = 'add ban data'
                logging = Log(userid=userid,date=date,time=time,detail=detail)
                logging.save()
                messages.success(request, 'แบนผู้ใช้สำเร็จ')
                return redirect("/banuserBoard")
        else:
            return redirect("/")

def banuserDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            banuser.objects.filter(id=id).delete()
            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'cancel ban data'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()
            return redirect("/banuserBoard")
        else:
            return redirect("/")

def roomBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            romdata = rooms.objects.all()
            return render(request,'roomBoard.html',{'romdata':romdata,'image':image})
        else:
            return redirect("/")

def roomAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            # max_id = rooms.objects.latest('id').id
            return render(request,'roomAdd.html',)
        else:
            return redirect("/")

def roomAddnewdata(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            rom_name = request.POST['rom_name']
            rom_topic = request.POST['rom_topic']
            rom_person = request.POST['rom_person']
            content = rooms(rom_name=rom_name,rom_topic=rom_topic,rom_person=rom_person)
            if(rooms.objects.filter(rom_name=rom_name)):
                messages.success(request, 'ชื่อห้องนี้ถูกใช้ไปแล้ว')
                return redirect("/roomAdd")
            else:     
                rounds_data = request.POST.getlist('room_start[]')
                time_start = request.POST.getlist('room_start[]')
                time_stop = request.POST.getlist('room_stop[]')
                count = 0
                checkstart = []
                xx = 0
                yy = 0
                for x in rounds_data:
                    if x < time_stop[xx]:
                        xx = xx+1
                        checkstart.append(x) 
                    else:
                        messages.success(request, 'เวลาเริ่มต้นต้องน้อยกว่าเวลาสิ้นสุด')
                        return redirect("/roomAdd")
                for y in range(1,len(time_start)):
                    tstart = datetime.datetime.strptime(time_start[y], "%H:%M")
                    tstop = datetime.datetime.strptime(time_stop[yy], "%H:%M")
                    dt = timedelta(minutes = 10)
                    end = tstop + dt
                    if tstart > end:
                        yy = yy+1
                        checkstart.append(y)
                    elif tstart > tstop and tstart < end:
                        messages.success(request, 'ช่วงเวลาแต่ละรอบต้องห่างกันอย่างน้อย 15 นาที')
                        return redirect("/roomAdd")   
                    else:
                        messages.success(request, 'เวลาเริ่มต้นรอบถัดไปต้องมากกว่ารอบก่อนหน้า')
                        return redirect("/roomAdd")        
                content.save()
                max_id = rooms.objects.latest('id').id


                for item in rounds_data:       
                    content2 = rounds.objects.create(
                        room_start = request.POST.get('room_start',item),
                        room_stop = time_stop[count],
                        room_id = max_id,              
                    )        
                    count = count + 1
                # type_data = request.POST.getlist('typeuser_id[]')
                # for item2 in type_data: 
                #     content3 = typeroom.objects.create(
                #         typeuser_id = request.POST.get('typeuser_id',item2),
                #         room_id = max_id,              
                #     )      
                userid = request.session.get('id')
                date = datetime.date.today()
                time = datetime.datetime.now()
                detail = 'add room data'
                logging = Log(userid=userid,date=date,time=time,detail=detail)
                logging.save()
                messages.success(request, 'บันทึกข้อมูลสำเร็จ')
                return redirect("/roomBoard")
          
        else:
            return redirect("/")

def roomEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = rooms.objects.filter(pk=id)
            room_round = rounds.objects.filter(room_id=id)
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'roomEdit.html',{'result':result,'room_round':room_round,'image':image})
        else:
            return redirect("/")

def roomUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id']
                rounds.objects.filter(room_id=id).delete()
                olddata = rooms.objects.get(pk = id)
                oldname = olddata.rom_name
                rom_name = request.POST['rom_name'] 
                rom_topic = request.POST['rom_topic']
                rom_person = request.POST['rom_person']
                content = rooms.objects.get(pk = id)
                content.rom_name = ' '
                content.save() 
                content = rooms.objects.get(pk = id)
                content.rom_name = rom_name
                content.rom_topic = rom_topic
                content.rom_person = rom_person
                result = rooms.objects.filter(pk=id)
                # check = request.POST.getlist('typeuser_id[]')
                # if check and check is not None and check != '':
                #     pass
                # else:
                #     content = rooms.objects.get(pk = id)
                #     content.rom_name = oldname
                #     content.save()
                #     types = typeuser.objects.all()
                #     room_round = rounds.objects.filter(room_id=id)
                #     type_room = typeroom.objects.filter(room_id=id)
                #     messages.success(request, 'กรุณาเลือกประเภทผู้ใช้')
                #     return render(request,'roomEdit.html',{'result':result,'room_round':room_round})


                if(rooms.objects.filter(rom_name=rom_name)):
                    content = rooms.objects.get(pk = id)
                    content.rom_name = oldname
                    content.save()
                    messages.success(request, 'ชื่อนี้ถูกใช้ไปแล้ว')    
                    emp_username = request.session.get('id_user')  
                    image = imagedata(emp_username)
                    return render(request, 'roomEdit.html',{'result':result,'image':image})  
                else:
                    rounds_data = request.POST.getlist('room_start[]')
                    time_start = request.POST.getlist('room_start[]')
                    time_stop = request.POST.getlist('room_stop[]')
                    checkstart = []
                    xx = 0
                    yy = 0
                    for x in rounds_data:
                        if x < time_stop[xx]:
                            xx = xx+1
                            checkstart.append(x) 
                        else:
                            content = rooms.objects.get(pk = id)
                            content.rom_name = oldname
                            content.save()
                            messages.success(request, 'เวลาเริ่มต้นต้องน้อยกว่าเวลาสิ้นสุด')
                            emp_username = request.session.get('id_user')  
                            image = imagedata(emp_username)
                            return render(request, 'roomEdit.html',{'result':result,'image':image})  
                    for y in range(1,len(time_start)):
                        if time_start[y] > time_stop[yy]:
                            yy = yy+1
                            checkstart.append(y)
                        else:
                            content = rooms.objects.get(pk = id)
                            content.rom_name = oldname
                            content.save()
                            messages.success(request, 'เวลาเริ่มต้นรอบถัดไปต้องมากกว่ารอบก่อนหน้า')
                            emp_username = request.session.get('id_user')  
                            image = imagedata(emp_username)
                            return render(request, 'roomEdit.html',{'result':result,'image':image})
                    content.save()
                    rounds_data = request.POST.getlist('room_start[]')
                    time_stop = request.POST.getlist('room_stop[]')
                    count = 0
                    for item in rounds_data: 
                        content2 = rounds.objects.create(
                            room_start = request.POST.get('room_start',item),
                            room_stop = time_stop[count],
                            room_id = id,              
                        )
                        count = count + 1    
                    type_data = request.POST.getlist('typeuser_id[]')
                    # for item2 in type_data: 
                    #     content3 = typeroom.objects.create(
                    #         typeuser_id = request.POST.get('typeuser_id',item2),
                    #         room_id = id,              
                    #     )
                    userid = request.session.get('id')
                    date = datetime.date.today()
                    time = datetime.datetime.now()
                    detail = 'edit room data'
                    logging = Log(userid=userid,date=date,time=time,detail=detail)
                    logging.save()
                    messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
                    reservation.objects.filter(rev_roomid=id).delete()
                    return redirect("/roomBoard")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")


def roomDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            rooms.objects.filter(id=id).delete()
            reservation.objects.filter(rev_roomid=id).delete()
            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'delete room data'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()
            return redirect("/roomBoard")
        else:
            return redirect("/")

def employeeBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            empdata = employee.objects.all()
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'employeeBoard.html',{'empdata':empdata,'image':image})
        else:
            return redirect("/")

def employeeAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'employeeAdd.html',{'image':image})
        else:
            return redirect("/")

def employeeAddnewdata(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            emp_username = request.POST['emp_username']
            emp_password = request.POST['emp_password']
            emp_prefix = request.POST['emp_prefix']
            emp_fname = request.POST['emp_fname']
            emp_lname = request.POST['emp_lname']
            emp_identification_code = request.POST['emp_identification_code']
            emp_bdate = request.POST['emp_bdate']
            emp_image = request.FILES['emp_image']
            status = 1
            content = employee(emp_username=emp_username,emp_password=emp_password,emp_prefix=emp_prefix,emp_fname=emp_fname,emp_lname=emp_lname,emp_identification_code=emp_identification_code,emp_bdate=emp_bdate,emp_image=emp_image,status_login=status)
    
            if(employee.objects.filter(emp_username=emp_username) or users.objects.filter(user_username=emp_username)):
                messages.success(request, 'Username นี้ถูกใช้ไปแล้ว')
                return redirect("/employeeAdd")
            elif(employee.objects.filter(emp_identification_code=emp_identification_code) or users.objects.filter(user_identification_code=emp_identification_code)):
                messages.success(request, 'รหัสประจำตัวประชาชนถูกใช้ไปแล้ว')
                return redirect("/employeeAdd")
            else:
                content.save()
                userid = request.session.get('id')
                date = datetime.date.today()
                time = datetime.datetime.now()
                detail = 'add employee data'
                logging = Log(userid=userid,date=date,time=time,detail=detail)
                logging.save()
                messages.success(request, 'บันทึกข้อมูลสำเร็จ')
                return redirect("/employeeBoard")
        else:
            return redirect("/")

def employeeEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = employee.objects.filter(pk=id)
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'employeeEdit.html',{'result':result,'image':image})
        else:
            return redirect("/")


def employeeUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id']
                olddata = employee.objects.get(pk=id)
                oldusername = olddata.emp_username
                oldidentification = olddata.emp_identification_code
                oldpassword = olddata.emp_password
                
                emp_username = request.POST['emp_username']
                emp_password = request.POST['emp_password']
                emp_prefix = request.POST['emp_prefix']
                emp_fname = request.POST['emp_fname']
                emp_lname = request.POST['emp_lname']
                emp_identification_code = request.POST['emp_identification_code']
                emp_bdate = request.POST['emp_bdate']
                try:
                    emp_image = request.FILES['emp_image']
                except KeyError:
                    emp_image = None
                content = employee.objects.get(pk=id)
                content.emp_username = ''
                content.emp_identification_code = ''
                content.save()
                content = employee.objects.get(id=id)
                content.emp_username = emp_username
                content.emp_password = emp_password
                content.emp_prefix =  emp_prefix
                content.emp_fname = emp_fname
                content.emp_lname = emp_lname
                content.emp_identification_code = emp_identification_code
                content.emp_bdate = emp_bdate
                result = employee.objects.filter(pk=id)
                if emp_image is not None:
                    employee.objects.get(id=id).emp_image.delete(save=True)
                    content.emp_image = emp_image   
                if(employee.objects.filter(emp_username=emp_username) or users.objects.filter(user_username=emp_username)):
                    content = employee.objects.get(pk = id)
                    content.emp_username = oldusername
                    content.emp_identification_code = oldidentification
                    content.save()
                    messages.success(request, 'Username นี้ถูกใช้ไปแล้ว')
                    emp_username = request.session.get('id_user')  
                    image = imagedata(emp_username)
                    return render(request, 'employeeEdit.html',{'result':result,'image':image})
                elif(employee.objects.filter(emp_identification_code=emp_identification_code and emp_username!=id) or users.objects.filter(user_identification_code=emp_identification_code)):
                    content = employee.objects.get(pk = id)
                    content.emp_username = oldusername
                    content.emp_identification_code = oldidentification
                    content.save()
                    messages.success(request, 'รหัสประจำตัวประชาชนถูกใช้ไปแล้ว')
                    emp_username = request.session.get('id_user')  
                    image = imagedata(emp_username)
                    return render(request, 'employeeEdit.html',{'result':result,'image':image})
                else:
                    content.save()
                    userid = request.session.get('id')
                    date = datetime.date.today()
                    time = datetime.datetime.now()
                    detail = 'edit employee data'
                    logging = Log(userid=userid,date=date,time=time,detail=detail)
                    logging.save()
                    messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
                    return redirect("/employeeBoard")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

def employeeDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            employee.objects.filter(id=id).delete()
            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'delete employee data'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()
            return redirect("/employeeBoard")
        else:
            return redirect("/")

def login(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return render(request,'login.html')
    else:
        if (x == 2):
            return render(request,'userindex.html',{})
        elif (x == 1):
            return render(request,'index.html',{})
        else:
            return redirect("/")

def requestdata(request):
    return render(request,'requestdata.html')

def register(request):
    try:
        if request.method == 'GET':    
            d = request.GET['university_code']
            p = request.GET['password']
            with urlopen("http://192.168.1.40:8085/"+d+p) as response:
                source = response.read()
            data = json.loads(source)
            user_password = data['user_password'].strip(" ' ")
            user_prefix = data['user_prefix'].strip(" ' ")
            user_firstname = data['user_firstname'].strip(" ' ")
            user_lastname = data['user_lastname'].strip(" ' ")
            user_bdate = data['user_bdate'].strip(" ' ")
            user_identification = data['user_identification'].strip(" ' ")
            user_university = data['user_university_code'].strip(" ' ")
            user_type = data['user_type'].strip(" ') ")
            if data:   
                return render(request,'register.html',{'user_password':user_password,'user_prefix':user_prefix,'user_firstname':user_firstname,'user_lastname':user_lastname,'user_bdate':user_bdate,'user_identification':user_identification,'user_university':user_university,'user_type':user_type})  
            else:
                messages.success(request, 'ไม่พบข้อมูลนักศึกษา')
            return redirect("/requestdata")
        else:
            pass
    except:
        if (messages == 'Username นี้ถูกใช้ไปแล้ว' or messages == 'บัญชีนี้ถูกใช้ไปแล้ว'):
            return redirect("/register")
        else:
            messages.success(request,'ไม่พบข้อมูลนักศึกษา')
            return redirect("/requestdata")

def registerNewdata(request):
    user_username = request.POST['user_username']
    user_password = request.POST['user_password']
    # user_password = make_password(password)
    user_prefix = request.POST['user_prefix']
    user_fname = request.POST['user_firstname']
    user_lname = request.POST['user_lastname']
    user_identification_code = request.POST['user_identification_code']
    user_university_code = request.POST['user_university_code']
    user_bdate = request.POST['user_bdate']
    user_image = request.FILES['user_image']
    user_type = request.POST['user_type']
    finger1 = None
    finger2 = None
    status = 2
    content = users(user_username=user_username,user_password=user_password,user_prefix=user_prefix,user_fname=user_fname,user_lname=user_lname,user_identification_code=user_identification_code,user_university_code=user_university_code,user_type=user_type,user_bdate=user_bdate,user_image=user_image,status_login=status,user_finger1=finger1,user_finger2=finger2)
    if(users.objects.filter(user_username=user_username) or employee.objects.filter(emp_username=user_username)):
        messages.success(request, 'Username นี้ถูกใช้ไปแล้ว')
        return redirect("/register")
    elif(users.objects.filter(user_identification_code=user_identification_code) or employee.objects.filter(emp_identification_code=user_identification_code)):
        messages.success(request, 'บัญชีนี้ถูกใช้ไปแล้ว')
        return redirect("/register")
    elif(users.objects.filter(user_university_code=user_university_code)):
        messages.success(request, 'บัญชีนี้ถูกใช้ไปแล้ว')
        return redirect("/register")    
    else:
        content.save()
        return redirect("/")

def logincheck(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        res = users.objects.filter(user_username=username,user_password=password).count()
        res2 = employee.objects.filter(emp_username=username,emp_password=password).count()
        if res > 0 and res2 == 0:
            data = users.objects.filter(user_username=username,user_password=password).get()
            request.session['logged_in']=data.status_login
            request.session['id_user']=data.user_username
            request.session['fname']=data.user_fname
            request.session['lname']=data.user_lname
            request.session['active']=data.user_status_finger
            request.session['id']=data.id
            userid = request.session['id']
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'login'
            content = Log(userid=userid,date=date,time=time,detail=detail)
            content.save()
            return redirect("/userindex")
        elif res2 > 0 and res == 0:
            data = employee.objects.filter(emp_username=username,emp_password=password).get()
            request.session['logged_in']=data.status_login
            request.session['id_user']=data.emp_username
            request.session['fname']=data.emp_fname
            request.session['lname']=data.emp_lname
            request.session['id']=data.id
            userid = request.session['id']
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'login'
            content = Log(userid=userid,date=date,time=time,detail=detail)
            content.save()
            return redirect("/index")
        else:
            messages.error(request,"ไม่พบผู้ใช้นี้")
            return redirect("/")
    return render(request, 'login.html')

def userindex(request):
    x = request.session.get('logged_in')
    user_username = request.session.get('id_user')

    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            image = userimagedata(user_username)
            userdata = users.objects.filter(user_username=user_username)
            reserve = reservation.objects.all()
            round = rounds.objects.all()
            
            resdata = reservation.objects.filter(rev_user=user_username)
            for data in resdata:
                re_id = data.id
                datecheck = data.rev_date
                today = datetime.date.today()
                #ลองเอา id ห้อง ไปหารอบ แล้วเอารอบมาคำนวณ
                if (today>=datecheck.date()):
                    statuschange = reservation.objects.get(pk=re_id)
                    statuschange.rev_status = 1 
                    statuschange.save()

            return render(request,'userindex.html',{'userdata':userdata,'image':image,'reserve':reserve,'round':round})
        else:
            return redirect("/")


def userEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = users.objects.filter(pk=id)
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'userEdit.html',{'result':result,'image':image})
        else:
            return redirect("/") 

def userUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id']
                olddata = users.objects.get(pk=id)
                oldusername = olddata.user_username
                oldpassword = olddata.user_password
                
                user_username = request.POST['user_username']
                user_password = request.POST['user_password']
                try:
                    user_image = request.FILES['user_image']
                except KeyError:
                    user_image = None
                content = users.objects.get(pk=id)
                content.user_username = ''
                content.save()
                content = users.objects.get(id=id)
                content.user_username = user_username
                content.user_password = user_password
                result = users.objects.filter(pk=id)
                if user_image is not None:
                    users.objects.get(id=id).user_image.delete(save=True)
                    content.user_image = user_image   
                if(users.objects.filter(user_username=user_username) or employee.objects.filter(emp_username=user_username)):
                    content = users.objects.get(pk = id)
                    content.user_username = oldusername
                    content.save()
                    messages.success(request, 'Username นี้ถูกใช้ไปแล้ว')
                    emp_username = request.session.get('id_user')  
                    image = imagedata(emp_username)
                    return render(request, 'userEdit.html',{'result':result,'image':image})
                else:
                    content.save()

                    userid = request.session.get('id')
                    date = datetime.date.today()
                    time = datetime.datetime.now()
                    detail = 'edit user profile'
                    logging = Log(userid=userid,date=date,time=time,detail=detail)
                    logging.save()

                    messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
                    return redirect("/userBoard")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")


def userpicEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            id = request.GET['id']
            result = users.objects.filter(pk=id)
            user_username = request.session.get('id_user')
            image = userimagedata(user_username)
            return render(request,'userpicEdit.html',{'result':result,'image':image})
        else:
            return redirect("/")     

def userpicUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            if request.method == 'POST':
                id = request.POST['id']
                olddata = users.objects.get(pk=id)
                oldusername = olddata.user_username
                oldpassword = olddata.user_password
                try:
                    user_image = request.FILES['user_image']
                except KeyError:
                    user_image = None
                content = users.objects.get(pk=id)
                content.user_username = ''
                content.save()
                content = users.objects.get(id=id)
                result = users.objects.filter(pk=id)
                if user_image is not None:
                    users.objects.get(id=id).user_image.delete(save=True)
                    content.user_image = user_image   
                else:
                    content.save()

                    userid = request.session.get('id')
                    date = datetime.date.today()
                    time = datetime.datetime.now()
                    detail = 'edit user picture profile'
                    logging = Log(userid=userid,date=date,time=time,detail=detail)
                    logging.save()
                    return redirect("/products")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

def userconfirmRoom(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            roombutton = rooms.objects.all()
            user_username = request.session.get('id_user')
            image = userimagedata(user_username)
            return render(request,'userconfirmRoom.html', {'roombutton': roombutton,'image':image})
        else:
            return redirect("/")

def userconfirmRoomSelected(request):
    x = request.session.get('logged_in')
    usernamecheck = request.session.get('id_user')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            if request.method == 'POST':
                selectrooms = request.POST.get('selectrooms', False)
                roomid = rooms.objects.filter(rom_name=selectrooms)
                for r in roomid:
                    room_id = r.id
 
                time = datetime.datetime.now()

                today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
                today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
                today = datetime.date.today()
                reservationdata  = reservation.objects.filter(rev_date__range=(today_min, today_max))
                
                
                roundsdata = rounds.objects.filter(Q(room_start__gte=time), Q(room_stop__lte=time))
                checkroom = []

                for x in roundsdata:
                    checkroom.append(x.room_id)

                for y in checkroom:
                    checkreserdata  = reservation.objects.filter(rev_roomid=y)
                    for z in checkreserdata:
                        testdata = z.rev_roomid
                        if room_id==z.rev_roomid:
                            messages.success(request, 'ห้องนี้กำลังอยู่ระหว่างการใช้งาน กรุณาเลือกห้องอื่น')
                            user_username = request.session.get('id_user')
                            image = userimagedata(user_username)
                            roombutton = rooms.objects.all()
                            return render(request, 'userconfirmRoom.html',{'roombutton':roombutton,'image':image})
                    
                # return render(request, 'testdata.html',{'selectrooms':room_id,'today_max':today_max,'today_min':today_min,'checkroom':checkroom,'reservationdata':reservationdata,'roundsdata':roundsdata})        

                if selectrooms == False :
                    messages.success(request, 'กรุณาเลือกห้องที่ต้องการทำการยืนยันลายนิ้วมือ')
                    user_username = request.session.get('id_user')
                    image = userimagedata(user_username)
                    roombutton = rooms.objects.all()
                    return render(request, 'userconfirmRoom.html',{'roombutton':roombutton,'image':image})
                else:
                    roomdata = rooms.objects.filter(rom_name=selectrooms)
                    roombutton = rooms.objects.all()
                    for data in roomdata :
                        room_id = data.id
                    r1 = requests.post("https://192.168.1.49:5000/get_my_ip", json={'data': room_id} ,verify = False)
                    ip_client = str(r1.json()['ip'])
                    # ip_client = 'สมมุติว่าเป็น ip_client'
                    user_username = request.session.get('id_user')
                    image = userimagedata(user_username)
                    return render(request,'userconfirm.html', {'room_id':room_id,'test_ip':ip_client,'roomdata':roomdata,'roombutton': roombutton,'image':image})
            elif request.method == 'GET': 
                pass
        else: 
            return redirect("/")

def userconfirmRoomSelected2(request):
    x = request.session.get('logged_in')
    usernamecheck = request.session.get('id_user')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            if request.method == 'POST':
                finger1 = request.POST['finger1']
                ip_client = request.POST['ip_client']
                room_id = request.POST['room_id']
                roomdata = rooms.objects.filter(id=room_id)
                user_username = request.session.get('id_user')
                image = userimagedata(user_username)
                if 'btn_click1' in request.POST:
                    while True:
                        scan1 = requests.get("http://"+str(ip_client)+":8081/")
                        if(scan1.text!=""):
                            res_scan1 = str(scan1.text)
                            break
                        time.sleep(20)
                    return render(request,'userconfirm.html', {'roomdata':roomdata,'room_id':room_id,'finger1':res_scan1,'test_ip':ip_client,'image':image})
                if 'submit' in request.POST:
                    return render(request,'userconfirm2.html', {'roomdata':roomdata,'room_id':room_id,'finger1':finger1,'test_ip':ip_client,'image':image})
            elif request.method == 'GET': 
                pass
        else: 
            return redirect("/")


def userAddconfirm(request):
    import time
    x = request.session.get('logged_in')
    usernamecheck = request.session.get('id_user')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            if request.method == 'POST':
                id = request.session.get('id_user')
                room_id = request.POST['room_id']
                roomdata = rooms.objects.filter(id=room_id)
                ip_client = request.POST['ip_client']
                finger1 = request.POST['finger1']
                finger2 = request.POST['finger2']
                
                content = users.objects.get(user_username = id)
                content.user_finger1 = finger1
                content.user_finger2 = finger2
                content.user_status_finger = True
                
                if 'btn_Click2' in request.POST:
                    while True:
                        scan2 = requests.get("http://"+str(ip_client)+":8081/")
                        if(scan2.text!=""):
                            res_scan2 = str(scan2.text)
                            break
                        time.sleep(20)
                    user_username = request.session.get('id_user')
                    image = userimagedata(user_username)
                    return render(request, 'userconfirm2.html',{'room_id':room_id,'roomdata':roomdata,'finger1':finger1,'finger2':res_scan2,'test_ip':ip_client,'image':image})
                   
                else:
                    if(finger1 == '' or finger1 == None or finger2 == '' or finger2 == None):
                        messages.success(request, 'กรุณายืนยันลายนิ้วมือก่อนบันทึก')
                        user_username = request.session.get('id_user')
                        image = userimagedata(user_username)
                        
                        return render(request, 'userconfirm2.html',{'room_id':room_id,'roomdata':roomdata,'finger1':finger1,'test_ip':ip_client,'image':image})
                    else:
                        messages.success(request, 'คุณได้ยืนยันลายนิ้วมือเรียบร้อยแล้ว')
                        content.save()
                        data = users.objects.filter(user_username=usernamecheck).get()
                        request.session['active']=data.user_status_finger

                        userid = request.session.get('id')
                        date = datetime.date.today()
                        time = datetime.datetime.now()
                        detail = 'confirm finger'
                        logging = Log(userid=userid,date=date,time=time,detail=detail)
                        logging.save()

                        return redirect("/userindex")
      
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")
    
def logout(request):
    userid = request.session.get('id')
    date = datetime.date.today()
    time = datetime.datetime.now()
    detail = 'logout'
    logging = Log(userid=userid,date=date,time=time,detail=detail)
    logging.save()
    del request.session['logged_in']
    del request.session['id_user']
    return redirect("/")

def userBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            userdata = users.objects.all()
            # typedata = typeuser.objects.all()
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'userBoard.html',{'userdata':userdata,'image':image})
        else:
            return redirect("/")

def adminconfirm(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = users.objects.filter(pk=id)
            emp_username = request.session.get('id_user')  
            image = imagedata(emp_username)
            return render(request,'adminconfirm.html',{'result':result,'image':image})
        else:
            return redirect("/")

def adminAddconfirm(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id_user']
                finger1 = request.POST['finger1']
                finger2 = request.POST['finger2']
                content = users.objects.get(id = id)
                content.user_finger1 = finger1
                content.user_finger2 = finger2
                content.user_status_finger = True
                
                if(finger1 == '' or finger1 == None or finger2 == '' or finger2 == None):
                    messages.success(request, 'กรุณายืนยันลายนิ้วมือก่อนบันทึก')
                    result = users.objects.filter(user_username=id)
                    emp_username = request.session.get('id_user')  
                    image = imagedata(emp_username)
                    return render(request,'adminconfirm.html',{'result':result,'image':image})
                else:
                    userid = request.session.get('id')
                    date = datetime.date.today()
                    time = datetime.datetime.now()
                    detail = 'add finger by admin'
                    logging = Log(userid=userid,date=date,time=time,detail=detail)
                    logging.save()

                    messages.success(request, 'ยืนยันลายนิ้วมือเรียบร้อยแล้ว')
                    content.save()
                    return redirect("/userBoard")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

def userDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            users.objects.filter(id=id).delete()
            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'delete user data'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()
            return redirect("/userBoard")
        else:
            return redirect("/")

def userReservation(request):
    x = request.session.get('logged_in')
    y = request.session.get('active')
    z = request.session.get('id_user')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            today = datetime.date.today()
            username = users.objects.filter(user_username=z)
            for userdata in username:
                userid = userdata.id
            if(banuser.objects.filter(ban_userid=userid)):
                bancheck = banuser.objects.filter(ban_userid=userid)
                for bandata in bancheck:
                    checkdate = bandata.ban_bdate
                    checkdays = bandata.ban_days
                lastdayban = checkdate + datetime.timedelta(days=checkdays)

                if (today<lastdayban.date()):
                    messages.success(request, 'คุณถูกระงับการใช้งานการจองเนื่องจากทำผิดกฎการใช้งาน กรุณาติดต่อเจ้าหน้าที่')
                    return redirect("/userindex")
                elif (today>=lastdayban.date()):
                    banuser.objects.filter(ban_userid=userid).delete()
                    if (y == 1):
                        allusers = users.objects.exclude(Q(user_username=z) | ~Q(user_status_finger=y))
                        allrooms = rooms.objects.all()
                        allrounds = rounds.objects.all()
                        user_username = request.session.get('id_user')
                        image = userimagedata(user_username)
                        return render(request,'userReservation.html',{'image':image,'allrooms':allrooms,'allusers':allusers, 'allrounds':allrounds})
                    else:
                        messages.success(request, 'คุณยังไม่ได้ยืนยันลายนิ้วมือ')
                        return redirect("/userindex")
            if (y == 1):
                allusers = users.objects.exclude(Q(user_username=z) | ~Q(user_status_finger=y))
                allrooms = rooms.objects.all()
                allrounds = rounds.objects.all()
                user_username = request.session.get('id_user')
                image = userimagedata(user_username)
                return render(request,'userReservation.html',{'image':image,'allrooms':allrooms,'allusers':allusers, 'allrounds':allrounds})
            else:
                messages.success(request, 'คุณยังไม่ได้ยืนยันลายนิ้วมือ')
                return redirect("/userindex")
        else:
            return redirect("/")

def userReservationAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            if request.method == 'POST':
                rev_userid = request.session.get('id_user')
                rev_roomid = request.POST.get('rev_roomid', False)
                rev_num = request.POST.get('rev_num', False)
                rev_date = request.POST['rev_date']
                rev_status = 0
                if rev_roomid == False or rev_num == False:
                    messages.success(request, 'กรุณากรอกข้อมูลให้ครบ')
                    return redirect("/userReservation")
                data = users.objects.get(user_username=rev_userid)
                content = reservation(rev_user=rev_userid,rev_roomid=rev_roomid,rev_date=rev_date,rev_num=rev_num,rev_status=rev_status)
                if(reservation.objects.filter(rev_roomid=rev_roomid) and reservation.objects.filter(rev_date=rev_date) and reservation.objects.filter(rev_num=rev_num)):
                    messages.success(request, 'คุณจองรอบที่ถูกจองไปแล้ว กรุณาจองรอบหรือห้องอื่น')
                    return redirect("/userReservation")
                content.save()
                max_id = reservation.objects.latest('id').id
                datedata = reservation.objects.filter(id=max_id)
                for d in datedata:
                    check = d.rev_date
                datecheck = check.date()
                today = datetime.date.today()
                if datecheck < today:
                    reservation.objects.latest('id').delete()
                    messages.success(request, 'กรุณาจองรอบของวันนี้เป็นต้นไป')
                    return redirect("/userReservation")
                users_datacheck = request.POST.getlist('user[]')
                users_data = []
                persondata = rooms.objects.get(id=rev_roomid)
                person = persondata.rom_person
                count = 1
                for x in users_datacheck:
                    count = count+1
                    if x not in users_data:
                        users_data.append(x)
                    else:
                        reservation.objects.latest('id').delete()
                        messages.success(request, 'กรุณาเชิญคนที่ไม่ซ้ำกัน')
                        return redirect("/userReservation")
                if count > person:
                    reservation.objects.latest('id').delete()
                    messages.success(request, 'ห้องนี้อนุญาติให้มีผู้ใช้ได้ไม่เกิน '+str(person)+' คน')
                    return redirect("/userReservation")
                for item in users_data:
                    content2 = roomuser.objects.create(
                        user = request.POST.get('user',item),
                        rev_id = max_id,    
                    )
                userid = request.session.get('id')
                date = datetime.date.today()
                time = datetime.datetime.now()
                detail = 'reservation room'
                logging = Log(userid=userid,date=date,time=time,detail=detail)
                logging.save()
                messages.success(request, 'ทำการจองห้องสำเร็จ') 
                return redirect("/userReservationBoard")
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")


def userReservationBoard(request):
    global idround
    x = request.session.get('logged_in')
    user = request.session.get('id_user')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            resdata = reservation.objects.filter(rev_user=user)
            user_username = request.session.get('id_user')
            image = userimagedata(user_username)
            return render(request,'userReservationBoard.html',{'resdata':resdata,'image':image})
        else:
            return redirect("/")

def userReservationDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            id = request.GET['id']
            reservation.objects.filter(id=id).delete()

            userid = request.session.get('id')
            date = datetime.date.today()
            time = datetime.datetime.now()
            detail = 'cancel reservation'
            logging = Log(userid=userid,date=date,time=time,detail=detail)
            logging.save()

            return redirect("/userReservationBoard")
        else:
            return redirect("/")

def load_courses(request):
    room_id = request.GET.get('rev_roomid')
    round = rounds.objects.filter(room_id=room_id)
    person = rooms.objects.filter(id=room_id)
    return render(request, 'courses_dropdown_list_options.html', {'round': round,'person':person})