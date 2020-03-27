from django.http import Http404
from rest_framework import serializers

from app_question.models import Answer
from app_question.models import Question
from app_question.models.answer import AnswerImage


class AnswerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerImage
        fields = ('image_url', 'seq',)


class AnswerSerializer(serializers.ModelSerializer):
    images = AnswerImageSerializer(many=True)
    author_display_name = serializers.SerializerMethodField()

    def get_author(self):
        request = self.context.get('request')

        if request is not None and hasattr(request, 'user'):
            return request.user
        return None

    def get_author_display_name(self, instance):
        return instance.author.display_name

    def create(self, validated_data):
        print(self.kwargs)
        user = self.get_author()
        if user is None:
            raise Http404()

        question_id = validated_data['question_id']
        content = validated_data['content']

        question = Question.objects.get(pk=question_id)
        answer = Answer.objects.create(
            question=question, author=user, content=content
        )

        for image in validated_data['images']:
            AnswerImage.objects.create(answer=answer, **image)

        return answer

    class Meta:
        model = Answer
        fields = ('content', 'images', 'created_at', 'updated_at',)
        read_only_fields = ('author_display_name', 'created_at', 'updated_at',)
