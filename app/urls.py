from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('add_grades/<int:pk>/', views.add_grades, name='add_grades'),
    path('grades_table/', views.grades_table, name='grades_table'),
    path('add_student/', views.add_student, name='add_student'),

]