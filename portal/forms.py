from django import forms
from .models import Unit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit 

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        # fields = ['unitName', 'courseDescription', 'requiredQualification', 'teachingMaterials',
        #          'sessionTimes', 'lecturer', 'lecturerEmail']
        fields  = ['name']

class RegistrationForm(UserCreationForm):
  

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PermanentStaffUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LoginForm(forms.Form): 
    username = forms.CharField(label="Username") 
    password = forms.CharField(widget=forms.PasswordInput(), label="Password") 

def __init__(self, *args, **kwargs): 
    super(LoginForm, self).__init__(*args, **kwargs) 
    self.helper = FormHelper() 
    self.helper.form_method = 'post' 
    self.helper.add_input(Submit('submit', 'Login')) 

def clean(self): 
    cleaned_data = super(LoginForm, self).clean() 
    username = cleaned_data.get('username') 
    password = cleaned_data.get('password') # Add validation as needed return cleaned_data