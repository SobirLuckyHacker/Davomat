from django.db import models

class Group_Student(models.Model):
    group_name=models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.group_name  
    

class Students(models.Model):
    name=models.CharField(max_length=150,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    group_choose=models.ForeignKey(Group_Student,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name


class Davomat(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    group =models.CharField(max_length=250,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name