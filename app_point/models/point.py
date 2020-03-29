from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Point(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.BigIntegerField(default=0, null=False)


class PointHistory(models.Model):
    pass
