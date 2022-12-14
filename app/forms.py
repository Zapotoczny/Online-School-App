from django import forms
from .models import Grades

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ['grade', 'grade_type']