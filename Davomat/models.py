from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Davomats(models.Model):
    name=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name