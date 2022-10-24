from pyexpat import model
from django.db import models

# Create your models here.


class ContactInfor(models.Model):
    address = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    open_hours = models.CharField(max_length = 255)


    def __str__(self) -> str:
        return self.address

class Subjects(models.Model):
    subject = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.subject

class ContactFromUser(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    subject = models.ForeignKey(Subjects,on_delete = models.CASCADE)
    phone = models.CharField(max_length = 255)
    message = models.TextField()


    def __str__(self) -> str:
        return self.name


