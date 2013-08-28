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
    nodename=models.CharField(max_length=40)
    ipv4=models.CharField(max_length=40,null=True)
    sshport=models.IntegerField(default='22')
    status=models.IntegerField(default='1')
    location=models.CharField(max_length=10,null=True)
    idcname=models.CharField(max_length=20,null=True)
    is_virtual=models.CharField(max_length=10)
    serialnumber=models.CharField(max_length=40,null=True)
    cpu_model=models.CharField(max_length=20)
    num_cpus=models.CharField(max_length=20)
    cpu_flags=models.CharField(max_length=200,null=True)
    harddisk=models.CharField(max_length=20)
    memory=models.CharField(max_length=20)
    ostype=models.CharField(max_length=20,null=True)
    os=models.CharField(max_length=20,null=True)
    os_family=models.CharField(max_length=20,null=True)
    kernel=models.CharField(max_length=20,null=True)
    kernelrelease=models.CharField(max_length=40,null=True)
    buytime=models.CharField(max_length=20,null=True)
    qualitytime=models.CharField(max_length=20,null=True)
    detail=models.CharField(max_length=200,null=True)

    def __unicode__(self):
        return self.nodename

class Ostype(models.Model):
    ostype=models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.ostype
class Idcnamelist(models.Model):
    idcname=models.CharField(max_length=50)
    usetime=models.CharField(max_length=40,null=True)
    detail=models.CharField(max_length=200,null=True)
    def __unicode__(self):
        return self.idcname

class Location(models.Model):
    location=models.CharField(max_length=50)
    detail=models.CharField(max_length=200,null=True)
    def __unicode__(self):
        return self.location

