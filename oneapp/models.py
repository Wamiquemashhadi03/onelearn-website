from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.TextField()
    # profile_image = models.ImageField(upload_to="Image")
    def __str__(self) -> str:
        return self.name
    


