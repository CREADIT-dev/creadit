from django.shortcuts import render

# Create your views here.
from rest_framework import serializers

from app_question.models.question import Question


class QuestionSeializer(serializers.ModelSerializer):
    class Meta:
        model = Question
