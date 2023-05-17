from django import forms
from .models import Unit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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