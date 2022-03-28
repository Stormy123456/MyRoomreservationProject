from django import forms2
from .models import CrudUser,employee,users,userinroomhistorys,roomhistorys

class RoomhistoryForm(forms2.ModelForm):
    class Meta:
        model = roomhistorys
        fields = ('id',)
