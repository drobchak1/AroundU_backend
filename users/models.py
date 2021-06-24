from django.db import models
from django.contrib.auth.models import AbstractUser
from versatileimagefield.fields import VersatileImageField, PPOIField


from AroundU import settings

class User(AbstractUser):
 ###################################################
 ###### THIS IS CODE FROM AbstractUser AND AbstractBaseUser FOR REFERENCE
 ###################################################
#  username_validator = UnicodeUsernameValidator()
#     password = models.CharField(_('password'), max_length=128)
#     last_login = models.DateTimeField(_('last login'), blank=True, null=True)
#     username = models.CharField(
#         _('username'),
#         max_length=150,
#         unique=True,
#         help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
#         validators=[username_validator],
#         error_messages={
#             'unique': _("A user with that username already exists."),
#         },
#     )
    first_name = models.CharField('first name', max_length=30, null=True, blank=True)
    last_name = models.CharField('last name', max_length=150, null=True, blank=True)
#     email = models.EmailField(_('email address'), blank=True)
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

# class ImageofUser(models.Model):
#     # name = models.CharField(max_length=255)
#     image = VersatileImageField(
#         'ImageofUser',
#         upload_to='imagesofuser/',
#         ppoi_field='image_ppoi'
#     )
#     image_ppoi = PPOIField()

#     def __str__(self):
#         return self.name
