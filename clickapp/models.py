from django.db import models

# Create your models here.
class photogdb(models.Model):
    PNAME=models.CharField(max_length=100,null=True,blank=True)
    PIM=models.ImageField(upload_to="pic",null=True,blank=True)
    desig=models.CharField(max_length=100,null=True,blank=True)
class savecatdb(models.Model):
    pcat=models.CharField(max_length=100,null=True,blank=True)
    pimg=models.ImageField(upload_to="pic",null=True,blank=True)
    pdes=models.CharField(max_length=100,null=True,blank=True)

class saveitemdb(models.Model):
    category_photo=models.CharField(max_length=100,null=True,blank=True)
    photo_name=models.CharField(max_length=100,null=True,blank=True)
    photo=models.ImageField(upload_to="pic",null=True,blank=True)
    p_description=models.CharField(max_length=100,null=True,blank=True)

class servicedb(models.Model):
    SNAME=models.CharField(max_length=100,null=True,blank=True)
    SIM=models.ImageField(upload_to="pic",null=True,blank=True)
    S_DESCRIPTION=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    time=models.CharField(max_length=100, null=True,blank=True)
    type=models.CharField(max_length=100,null=True,blank=True)

# events/models.py


class Event(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()







