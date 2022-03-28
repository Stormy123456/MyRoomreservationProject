from django.http import HttpResponse, response
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from.models import employee,Log,codeurl,idcode,users,reservation,rooms,rounds,roomuser,CrudUser,banuser,roomhistorys,userinroomhistorys,offender,banuser,punishment,testhistroys,testinroomhistroys
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

from pprint import pprint
#from urllib.request import Request, urlopen
from django.views.generic import ListView
from django.views.generic import View
from .forms import BookForm
from .forms import ProductForm
from datetime import date, timedelta
from django.http import JsonResponse
import json
from store import views
from rest_framework.response import Response
from rest_framework.views import APIView



def userToken(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            user_username = request.session.get('id_user')
            image = views.userimagedata(user_username)
            return render(request,'userToken.html',{'image':image})
        else:
            return redirect("/")

def userTokenAdd(request):
    redirect_uri = 'http://localhost:8001/userToken'
    client_id = 'XO8DIZFf8qIb41yk7zCoSz'
    client_secret = 'VMfx9IBbq6Vql5syAMVFRBf7Sqf7DhSV4BeW7ikzZEQ'

    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/") 
    else:
        if (x == 2):
            if request.method == 'POST':
                userid = request.session.get('id_user')
                code_url2 = request.POST['code_url2']

                response = requests.post('https://notify-bot.line.me/oauth/token', data ={'grant_type':'authorization_code','code': code_url2,'redirect_uri': redirect_uri,'client_id': client_id,'client_secret': client_secret })
                loadedJson = json.loads(response.text)
                code_token = loadedJson['access_token']

                code_url = str(code_token)
                content = users.objects.get(user_username = userid)
                content.code_urluser_token = code_url
                content.save() 
                messages.success(request, 'คุณได้ยืนยัน Line เรียบร้อยแล้ว')
                return redirect("/userToken") 
                # if(codeurl.objects.filter(userid=userid)):
                #     content = codeurl.objects.get(userid = userid)
                #     content.code_url = code_url
                #     content.save() 
                #     messages.success(request, 'คุณได้ยืนยัน Line เรียบร้อยแล้ว')
                #     return redirect("/userToken") 
                # else: 
                #     content = codeurl(userid=userid,code_url=code_url)
                #     content.save()
                #     messages.success(request, 'คุณได้ยืนยัน Line เรียบร้อยแล้ว')
                #     return redirect("/userToken")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")