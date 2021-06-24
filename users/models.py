from django.db import models
from django.contrib.auth.models import AbstractUser
from versatileimagefield.fields import VersatileImageField, PPOIField


from AroundU import settings

class User(AbstractUser):
    first_name = models.CharField('first name', max_length=30, null=True, blank=True)
    last_name = models.CharField('last name', max_length=150, null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    # image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    image = VersatileImageField(
        'ImageofUser',
        upload_to='imagesofuser/',
        ppoi_field='image_ppoi',
        blank=True,
        null=True,
    )
    image_ppoi = PPOIField()
