from django.http import HttpResponse, response
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from.models import employee,Log,idcode,users,reservation,rooms,rounds,roomuser,CrudUser,banuser,roomhistorys,userinroomhistorys,offender,banuser,punishment,testhistroys,testinroomhistroys
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

from pprint import pprint
from urllib.request import Request, urlopen
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



class TestViews(APIView):
    def get(self,request,*args,**kwargs):
        response = dict(status='Success',result='Get')
        return Response(response, 200)

    def post(self,request,*args,**kwargs):
        response = dict(status='Success',result='Post')
        return Response(response, 200)


    
def historyLog(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            emp_username = request.session.get('id_user')  
            image = views.imagedata(emp_username)
            logdata = Log.objects.all().order_by('-id')
            return render(request,'historyLog.html',{'image':image,'logdata':logdata})
        else:
            return redirect("/")