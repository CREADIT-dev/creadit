from rest_framework import serializers

from app_question.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer

