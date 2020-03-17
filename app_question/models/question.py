from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Question(models.Model):
    class Category(models.TextChoices):
        EDITING = '편집'
        COPYRIGHT = '저작권'
        CHANNEL_MANAGEMENT = '채널관리'
        ETC = '기타'

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.CharField(max_length=15, choices=Category.choices, db_index=True)
    content = models.TextField()


class QuestionImage(models.Model):
    question = models.ForeignKey(Question, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
    seq = models.IntegerField()
