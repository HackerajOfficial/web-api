from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    ROLES               =   (("0","Admin"),("1","journalist"),("2","staff"))
    role                =   models.CharField(choices=ROLES, max_length=2, default="0")
    email               =   models.CharField(max_length=50,unique=True)

    USERNAME_FIELD      =   "email"   #if i have to login using email then use "email" , if from username then put username
    REQUIRED_FIELDS     =   ["username","role"] #username_fields element does not used in required field



class UserProfile(models.Model):
    user                =   models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    address             =   models.CharField(max_length=100)
    profile_pic         =   models.ImageField(upload_to='uploads')
