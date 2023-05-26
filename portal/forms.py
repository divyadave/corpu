from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit 

from .models import JobListing
from .models import CreateJob
from .models import Staff, SessionalStaffUser

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = CreateJob
        fields = ['unit_name', 'course_description', 'required_qualification', 'teaching_materials', 'session_times', 'responsibilities', 'benefits']

class CreateProfile(forms.ModelForm):
    class Meta:
        model = SessionalStaffUser
        fields = ['first_name', 'last_name', 'email', 'qualifications', 'availability', 'phoneno', 'dob', 'gender', 'certification', 'work_experience', 'week_availability', 'days_of_week', 'timing', 'preferred_unit', 'preferred_location' , 'preferred_teaching_styles']

    
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]


class PermanentStaffUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LoginForm(forms.Form): 
    username = forms.CharField(label="Username") 
    password = forms.CharField(widget=forms.PasswordInput(), label="Password") 

def _init_(self, *args, **kwargs): 
    super(LoginForm, self)._init_(*args, **kwargs) 
    self.helper = FormHelper() 
    self.helper.form_method = 'post' 
    self.helper.add_input(Submit('submit', 'Login')) 

def clean(self): 
    cleaned_data = super(LoginForm, self).clean() 
    username = cleaned_data.get('username') 
    password = cleaned_data.get('password') # Add validation as needed return cleaned_data