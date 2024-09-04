from django import forms 
from django.core import validators
from django.contrib.auth.models import User
from .models import User_model, UserInfoModel

#user model practice level5 
class UserInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
#user model practice level5 
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfoModel
        fields = ('linkedin_link', 'profile_pic')


class info_form (forms.Form):
    name = forms.CharField()
    email = forms.CharField(max_length= 300, required=True)
    bio = forms.CharField(widget = forms.Textarea) 
    botcatcher = forms.CharField(required= False, widget= forms.HiddenInput)
    
    
#to connect a model with the form 
class Registeration(forms.ModelForm):
    class Meta:
        model = User_model
        fields = '__all__'
    