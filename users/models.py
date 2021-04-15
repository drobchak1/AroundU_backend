from django.db import models
from django.contrib.auth.models import AbstractUser

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
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=150, blank=True)
#     email = models.EmailField(_('email address'), blank=True)
    bio = models.TextField()
    city = models.CharField(max_length=20)
    # image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    city = models.CharField(max_length=50)
