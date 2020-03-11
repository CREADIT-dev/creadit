from rest_framework import serializers

from app_question.models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
