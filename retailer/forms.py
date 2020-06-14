from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    class Meta:
        model = User
        fields = ("username","email",'password1','password2')

class MyAccountForm(forms.ModelForm):
    class Meta:
        model = Shop
        exclude = ('user','city','state')  

class EmployeeRegisterForm(forms.ModelForm):
    class Meta:
        model= Employee 
        exclude = ('user','last_updated','date_joined')

class ItemRegisterForm(forms.ModelForm):
    class Meta:
        model = Item 
        exclude= ('user', )

class NoteRegisterForm(forms.ModelForm):
    class Meta:
        model = Note 
        exclude =('user','created_on')
