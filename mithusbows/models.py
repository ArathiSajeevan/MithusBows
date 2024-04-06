from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#user registration
class regmodel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


#admin registration
class adminregmodel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

#item database
class item(models.Model):
    image = models.FileField(upload_to="mithusbows/static")
    itemname = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    price = models.IntegerField()

