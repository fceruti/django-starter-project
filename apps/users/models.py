from django.contrib.auth.models import (
    AbstractBaseUser, Group as BaseGroup, PermissionsMixin)
from django.db import models
from django.utils import timezone
from registration.models import RegistrationProfile as BaseRegistrationProfile

from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def full_name(self):
        return self.email

    def short_name(self):
        return self.email

    def get_username(self):
        return self.email


class Group(BaseGroup):
    class Meta:
        proxy = True


class RegistrationProfile(BaseRegistrationProfile):
    class Meta:
        proxy = True
