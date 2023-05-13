from django import forms
from .models import Unit


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unitName', 'courseDescription', 'requiredQualification', 'teachingMaterials',
                  'sessionTimes', 'lecturer', 'lecturerEmail']
