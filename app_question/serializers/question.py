from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import serializers

from app_question.models import QuestionImage
from app_question.models.question import Question

User = get_user_model()


class QuestionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionImage
        fields = ('image_url', 'seq',)


class QuestionSerializer(serializers.ModelSerializer):
    images = QuestionImageSerializer(many=True)
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'author', 'point', 'category', 'content', 'images', 'like_count', 'created_at', 'updated_at')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at')

    def get_author(self):
        request = self.context.get('request')

        if request is not None and hasattr(request, 'user'):
            return request.user
        return None

    def get_like_count(self, instance):
        return instance.likes.count()

    def create(self, validated_data):
        user = self.get_author()
        if user is None:
            raise Http404()

        point = validated_data['point']
        category = validated_data['category']
        content = validated_data['content']
        question = Question.objects.create(author=user, point=point, category=category, content=content)

        for image in validated_data['images']:
            QuestionImage.objects.create(question=question, **image)

        return question

    def update(self, instance, validated_data):
        point = validated_data['point']
        category = validated_data['category']
        content = validated_data['content']
        
        instance.point = point
        instance.category = category
        instance.content = content
        instance.save()

        image_qs = QuestionImage.objects.filter(question=instance)
        for image_data in validated_data['images']:
            image_url = image_data['image_url']
            seq: int = image_data['seq']

            if image_qs.filter(seq=seq).exists():
                image: QuestionImage = image_qs.get(seq=seq)
                image.image_url = image_url
                image.save()
            else:
                QuestionImage.objects.create(question=instance, image_url=image_url, seq=seq)

        return instance
