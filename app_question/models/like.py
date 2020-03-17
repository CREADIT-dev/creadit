from django.contrib.auth import get_user_model
from django.db import models

from app_question.models.question import Question

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'question_like'
