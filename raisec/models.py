
from django.db import models


# Create your models here.
class RaisecGroup(models.Model):
    group_name = models.CharField(max_length = 255)
    

    def __str__(self) -> str:
        return self.group_name



class RaisecQuestions(models.Model):
    raisec_category = models.ForeignKey(RaisecGroup,on_delete = models.CASCADE)
    raisec_question = models.CharField(max_length = 255)


    def __str__(self) -> str:
        return self.raisec_question







    


