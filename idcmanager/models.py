from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=200)
    #password_two=models.CharField(max_length=200)
    age=models.CharField(max_length=10)
    sex=models.CharField(max_length=10)

    def __unicode__(self):
        return self.username
class Idcmanager(models.Model):
    hostname=models.CharField(max_length=40)
    ip=models.CharField(max_length=40)
    serialnumber=models.CharField(max_length=40)
    sshport=models.IntegerField(default='22')
    status=models.IntegerField(default='1')
    location=models.CharField(max_length=10)
    idcname=models.CharField(max_length=20)
    ostype=models.CharField(max_length=20)
    cpu=models.CharField(max_length=20)
    harddisk=models.CharField(max_length=20)
    memory=models.CharField(max_length=20)
    buytime=models.CharField(max_length=20)
    qualitytime=models.CharField(max_length=400)
    detail=models.CharField(max_length=200)

    def __unicode__(self):
        return self.hostname

class Ostype(models.Model):
    ostype=models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.ostype
