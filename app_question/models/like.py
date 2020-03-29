from django.contrib.auth import get_user_model
from django.db import models

from app_question.models import Answer
from app_question.models.question import Question

User = get_user_model()


class QuestionLike(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'question_like'
        unique_together = ('user', 'question',)


class AnswerLike(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'answer_like'
        unique_together = ('user', 'answer',)
