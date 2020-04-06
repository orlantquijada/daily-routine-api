from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from backend import mixins
from backend.utils import global_vars

from backend.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, mixins.NameMixin):

    username = models.CharField(
        max_length=global_vars.NAME_MAX_LENGTH, unique=True)

    profile_pic = models.ImageField('Profile Picture',
                                    upload_to='users/profile-pics/', blank=True, null=True)

    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    def __str__(self):
        # pylint: disable=no-member
        return f'{self.id} / {self.username} / {self.full_name()}'
