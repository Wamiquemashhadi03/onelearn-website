from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default= 'your name', max_length=100, null=True)
    phone = models.CharField(default= 'your phone',max_length=12, null=True)
    country = models.CharField(default= 'your country',max_length=50, null=True)
    state = models.CharField(default= 'your state',max_length=50, null=True)
    address = models.TextField(default= 'your address',max_length=200, null=True)
    profile_image = models.ImageField(default= 'media/default.jpg', upload_to='media', null=True, blank=True)
    # profile_image = models.ImageField(upload_to="Image")
    def __str__(self):
        return f"{self.user.username}'s profile"
    


