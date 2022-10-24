from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from raisec.models import RaisecGroup,RaisecQuestions


class UserTable(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.CharField(null=True,max_length=255)
    
    
    
    REQUIRED_FIELDS = ['username','phone','first_name','last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class UserProfile(models.Model):
    raisec = models.ForeignKey(RaisecGroup,on_delete = models.CASCADE)
    user = models.ForeignKey(UserTable,on_delete = models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)
   


class RaisecAnswer(models.Model):
    user = models.ForeignKey(UserTable,on_delete = models.CASCADE)
    quiz =  models.ForeignKey(RaisecQuestions,on_delete = models.CASCADE)
    raisec_answer = models.BooleanField(default = False)

    def __str__(self) -> str:
        return str(self.quiz)


