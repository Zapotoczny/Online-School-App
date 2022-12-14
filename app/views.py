from django.shortcuts import redirect, render
from .models import Students, Grades
from django.db.models import Avg
from .forms import GradeForm, AddStudentForm

# Create your views here.

def class_list(request):
    students = Students.objects.all()
    return render(request, 'class_list.html',{'students':students})

def add_grades(request,pk):
    name = Students.objects.get(pk=pk)

    #Get student with same id
    stu_id = Students.objects.get(pk=pk).student_id
    grades = Grades.objects.filter(student_id=stu_id)

    #Get avg
    avg_grades = Grades.objects.filter(student_id=stu_id).aggregate(Avg('grade'))['grade__avg']

    #Save to db if methode POST and form is valid
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            add_grade = form.save(commit=False)
            add_grade.student_id = Students.objects.get(pk=pk).student_id
            add_grade.save()
            return redirect('add_grades', pk=pk)
    else:
        form = GradeForm()
        
    return render(request, 'add_grades.html', {'form':form,'name':name,'grades':grades,'avg_grades':avg_grades,'student_id':stu_id})

def grades_table(request):
    table = []
    students = Students.objects.all()
    for student in students:

        #Add students with values
        resault ={
            'name':student.name,
            'avg':Grades.objects.filter(student_id=student.student_id).aggregate(Avg('grade'))['grade__avg'] or 0,
            'id':student.student_id
        }

        #Append to main table
        table.append(resault)

    return render(request, 'grades_table.html', {'table':table})

def add_student(request):
    #Check if request method is POST and is valid then add new student
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student_form = form.save(commit=False)
            student_form.save()
            return redirect('/')
    else:
        form = AddStudentForm()
    return render(request, 'add_student.html', {'form':form})