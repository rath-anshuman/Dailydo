from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)

    def __str__(self) :
        return self.title





#---------------------For Api -------------------------


from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'