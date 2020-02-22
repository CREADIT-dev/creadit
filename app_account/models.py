from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        pass

    def create_superuser(self, name, email, nickname, password):
        pass


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=10, null=False, verbose_name='유저의 실명')
    email = models.EmailField(max_length=50, unique=True, verbose_name='유저의 이메일')
    display_name = models.CharField(max_length=20, null=False, verbose_name='유저의 닉네임')
    point = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'email', 'display_name']
