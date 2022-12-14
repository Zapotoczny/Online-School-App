from django import forms
from .models import Grades, Students

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ['grade', 'grade_type']

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'last_name', 'class_number']