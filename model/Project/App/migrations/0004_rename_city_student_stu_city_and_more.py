# Generated by Django 5.0.7 on 2024-07-23 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_student_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='City',
            new_name='Stu_City',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Contact',
            new_name='Stu_Contact',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='Stu_Email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Name',
            new_name='Stu_Name',
        ),
    ]
