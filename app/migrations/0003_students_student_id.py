# Generated by Django 4.1.4 on 2022-12-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_students_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='student_id',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]