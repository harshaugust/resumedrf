from distutils.command.upload import upload
from django.db import models

# Create your models here.

STATE_CHOICES = ((
    ('Bihar','Bihar'),
    ('Uttarpradesh','Uttarpradesh'),
    ('West Bengal', 'West Bengal')
))

GENDER = ((
    ('male', 'male'),
    ('female', 'female')
))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now= False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICES, max_length= 100)
    gender = models.CharField(choices = GENDER, max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to = 'pimages', blank = True)
    rdoc = models.FileField(upload_to = 'rdocs',  blank = True)

    