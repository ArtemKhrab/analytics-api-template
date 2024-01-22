from .managers import UserManager

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_request = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    def __str__(self):
        return " ".join([str(self.id), self.username, "admin: ", str(self.is_admin)])

    def has_perm(self, *args, **kwargs):
        return self.is_admin

    def has_module_perms(self, *args, **kwargs):
        return True
