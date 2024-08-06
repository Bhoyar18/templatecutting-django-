from django.db import models

# Create your models here.
# class Student(models.Model):
#     Name=models.CharField(max_length=70)
#     Email=models.EmailField()
#     Contact=models.IntegerField()
#     City=models.CharField(max_length=50)

#     def __str__(self):
#         return self.Name+' '+self.Email
    # for changing the name .......
    # class Meta:
    #     db_table = 'Student'
        # django by default verbose name me 's' add krke deta hai 
        # verbose_name = 'Student'
        # we can give any name accordingly through this command 
        # verbose_name_plural = 'Student'
        
        # for changing name of students in decending order we use (-) sign 
        # ordering = ['-Name']

        # for changing in ascending order we will remove the  (-)sign
        # ordering = ['Name']

# ==================================================================================


class Student(models.Model):
    Stu_Name=models.CharField(max_length=70)
    Stu_Email=models.EmailField()
    Stu_Contact=models.IntegerField()
    Stu_City=models.CharField(max_length=50)

    def __str__(self):
        return self.Stu_Name
    
    class Meta:
        db_table = 'Student'