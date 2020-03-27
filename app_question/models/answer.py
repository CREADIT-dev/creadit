from django.contrib.auth import get_user_model
from django.db import models

from app_question.models.question import Question

User = get_user_model()


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'answer'


class AnswerImage(models.Model):
    answer = models.ForeignKey(Answer, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()
    seq = models.IntegerField()

    class Meta:
        db_table = 'auswer_image'
