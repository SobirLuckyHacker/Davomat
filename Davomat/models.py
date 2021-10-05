from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=150,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    
class Davomats(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name