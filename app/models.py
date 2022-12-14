import random
from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    class_number = models.IntegerField(null=False)
    student_id = models.CharField(max_length=8,blank=True,default='xyz')

    def save(self, *args, **kwargs):
        self.student_id = f"{(str(self.name))[:3].lower()}{str(self.last_name)[:3].lower()}{self.class_number}"
        super(Students, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

class Grades(models.Model):
    grade = models.IntegerField()
    # 0 - test  1 - exam  2 - answer
    grade_type = models.CharField(max_length=8)
    student_id = models.CharField(max_length=8)