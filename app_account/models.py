from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, display_name, password=None):
        if email is None:
            return

        user = self.model(
            email=self.normalize(),
            display_name=display_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, display_name, password=None):
        user = self.create_user(email, display_name, password)
        user.is_staff = True


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=10, null=False, verbose_name='유저의 실명')
    email = models.EmailField(max_length=50, unique=True, null=False, verbose_name='유저의 이메일')
    display_name = models.CharField(max_length=20, null=False, verbose_name='유저의 닉네임')
    point = models.IntegerField()
    is_admin = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['name', 'display_name']
    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user'
        verbose_name = ('user',)
        verbose_name_plural = ('users',)
        swappable = 'AUTH_USER_MODEL'
