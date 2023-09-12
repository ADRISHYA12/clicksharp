from django.db import models

# Create your models here.
class registerdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=70,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=70,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)

class appoitment(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    mobile=models.CharField(max_length=1000,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    typeofservice=models.CharField(null=True,blank=True,max_length=100)
    duration=models.CharField(max_length=100,null=True,blank=True)
    remarks=models.CharField(max_length=1000,null=True,blank=True)









