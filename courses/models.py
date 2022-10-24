from email.policy import default
from hashlib import blake2b
from operator import truediv
from pickle import TRUE
from statistics import mode
from django.db import models
from accounts.models import UserTable
import os
import random
from django.utils import timezone
from raisec.models import RaisecGroup

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "courses/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )


class ClusterClasses(models.Model):
    category_name = models.CharField(max_length  = 255)



    def __str__(self) -> str:
        return self.category_name


class MinimumRequirement(models.Model):
    grade = models.CharField(max_length =  3)
    mimimum_point = models.PositiveBigIntegerField(default  = 0)
    maximum_point =  models.PositiveBigIntegerField(default = 0)


    def __str__(self) -> str:
        return self.grade


class UserMinimumRequirement(models.Model):
    user = models.ForeignKey(UserTable,on_delete = models.CASCADE)
    minimum_requirement =  models.ForeignKey(MinimumRequirement,on_delete = models.CASCADE,blank = True,null = True)

    def __str__(self) -> str:
        return str(self.user)






class Course(models.Model):
    user = models.ForeignKey(UserTable,on_delete = models.CASCADE , blank  = True , null = True)
    raisec_group =  models.ForeignKey(RaisecGroup,on_delete = models.CASCADE , blank  = True , null = True)
    cluster_name = models.ForeignKey(ClusterClasses,on_delete = models.CASCADE,blank= True,null = True)
    university = models.CharField(max_length =  255)
    course_title = models.CharField(max_length =  255)
    course_image = models.ImageField(upload_to =  upload_image_path)
    short_description = models.CharField(max_length = 255 , blank = True,null = True)
    course_description =  models.TextField()
    ratting_percentage = models.PositiveBigIntegerField(blank = True,null = True)
    miniumu_requirement = models.ForeignKey(MinimumRequirement,on_delete = models.CASCADE,blank= True,null = True)
    is_published = models.BooleanField(default = True)
    is_instructor = models.BooleanField(default = False)


    def __str__(self) -> str:
        return self.course_title



class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()



class CourseRattingAndComment(models.Model):
    user = models.ForeignKey(UserTable,on_delete = models.CASCADE , blank  = True , null = True)
    course = models.ForeignKey(Course,on_delete = models.CASCADE)
    ratings = models.PositiveBigIntegerField()
    comment = models.CharField(max_length =  255)
    created_at = models.DateField(default=timezone.now,editable = False)
    updated_at = AutoDateTimeField(default=timezone.now,editable = False)


    def __str__(self) -> str:
         return str(self.course)







class AdvertUserLinks(models.Model):
    user_image = models.ImageField(upload_to =  upload_image_path)
    ig_link = models.URLField()

    def __str__(self) -> str:
        return self.ig_link



    


