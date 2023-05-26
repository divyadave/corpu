from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

from .models import JobListing
from .models import CreateJob
from .models import Staff


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = CreateJob
<<<<<<< HEAD
        fields = ['unit', 'course_description', 'required_qualification',
                  'teaching_materials', 'session_times', 'responsibilities', 'benefits']

=======
        fields = ['course_description', 'required_qualification', 'teaching_materials', 'session_times', 'responsibilities', 'benefits']
>>>>>>> 334c92b0b1c94dcc2ffe6e56eab063f3e739840c

class CreateProfile(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = Unit
        # fields = ['unitName', 'courseDescription', 'requiredQualification', 'teachingMaterials',
        #          'sessionTimes', 'lecturer', 'lecturerEmail']
        fields = ['UnitName', 'CourseDescription', 'RequiredQualification']


=======
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'qualifications', 'availability', 'phoneno', 'dob', 'gender', 'certification', 'work_experience']
    
>>>>>>> 334c92b0b1c94dcc2ffe6e56eab063f3e739840c
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
    # Add validation as needed return cleaned_data
    password = cleaned_data.get('password')
