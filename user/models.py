from django.db import models

# Create your models here.
class Profile(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        )
    Blood_group = (
        ('A+','A+'),
        ('A-','A+'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'),
    )

    Religion = (
        ('Islam','Islam'),
        ('Hindu','Hindu'),
        ('Cristian','Cristian'),
        ('Buddha','Buddha'),
        ('Others','Others'),
    )
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='profile_pic/',default="def.png")
    email = models.EmailField(max_length=30)
    gender = models.CharField(choices=Gender ,max_length=8,default='----')
    address = models.TextField(max_length=50)
    religion = models.CharField(choices=Religion,max_length=10,default='-----')
    blood_group = models.CharField(choices=Blood_group,max_length=4,default='----')
    Date_of_birth = models.DateField()
    is_alive = models.BooleanField(default=False , null=True)
    def __str__(self) -> str:
        return self.name
    
class del_profile(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="profile_pics/",default='def.png')
    email = models.EmailField(max_length=30)
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=40)
    religion =models.CharField(max_length=10)
    blood_group =models.CharField(max_length=4)
    date_of_birth = models.DateField()
    is_alive = models.BooleanField(default=False ,null= True)
    previous_id = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.name