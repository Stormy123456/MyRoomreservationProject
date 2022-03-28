from django import forms
from .models import CrudUser,employee,users,userinroomhistorys,roomhistorys

class BookForm(forms.ModelForm):
	publication_date = forms.DateTimeInput()
	class Meta:
		model = CrudUser
		fields = ('name', 'address', 'age')

class ProductForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ('user_username', 'user_password')

class RoomhistoryForm(forms.ModelForm):
    class Meta: 
        model = userinroomhistorys
        fields = ('Username','timescan')
       
       
        

