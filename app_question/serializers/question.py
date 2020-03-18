from typing import Optional

from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from app_question.models import QuestionImage
from app_question.models.question import Question

User = get_user_model()


class QuestionImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionImage
        fields = ('question', 'image', 'seq',)


class QuestionSerializer(serializers.ModelSerializer):
    images = QuestionImageSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('author', 'category', 'content', 'images', 'created_at', 'updated_at')
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_author(self):
        request = self.context.get('request')

        if request is not None and hasattr(request, 'user'):
            return request.user
        return None

    def create(self, validated_data):
        user = self.get_author()
        if user is None:
            raise Http404()

        user = User.objects.get(email=user.email)
        return Question.objects.create(author=user, **validated_data)
