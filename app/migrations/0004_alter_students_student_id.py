# Generated by Django 4.1.4 on 2022-12-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_students_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.CharField(blank=True, default='xyz', max_length=8),
        ),
    ]