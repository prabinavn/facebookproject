from django.db import models

# Create your models here.
class Login(models.Model):
    username  = models.CharField(max_length=30,unique=True)
    password  = models.CharField(max_length=20,unique=True)

class Register(models.Model):
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    dob       = models.DateField()
    gender    = models.CharField(max_length=20)
    loginForm = models.ForeignKey(Login,on_delete=models.CASCADE)


class Profile_Pic(models.Model):
    image = models.FileField(upload_to='profilepics/')
    fk_login = models.ForeignKey(Login, on_delete=models.CASCADE)

    
