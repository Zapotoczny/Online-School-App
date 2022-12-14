from django.shortcuts import redirect, render
from .models import Students, Grades
from .forms import GradeForm

# Create your views here.

def class_list(request):
    students = Students.objects.all()
    return render(request, 'class_list.html',{'students':students})

def add_grades(request,pk):
    name = Students.objects.get(pk=pk)
    grades = Grades.objects.filter(student_id=Students.objects.get(pk=pk).student_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            add_grade = form.save(commit=False)
            add_grade.student_id = Students.objects.get(pk=pk).student_id
            add_grade.save()
            return redirect('add_grades', pk=pk)
    else:
        form = GradeForm()
    return render(request, 'add_grades.html', {'form':form,'name':name,'grades':grades})

def grades_table(request):
    return render(request, 'grades_table.html')