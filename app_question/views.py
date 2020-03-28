from django.http import Http404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from app_question.models import Answer
from app_question.models import Like
from app_question.models.question import Question
from app_question.serializers.answer import AnswerSerializer
from app_question.serializers.question import QuestionSerializer
from mixin import AllowModifyOnlyAuthorUserMixin, LoginRequiredMixin


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (LoginRequiredMixin, AllowModifyOnlyAuthorUserMixin,)
    lookup_url_kwarg = "question_id"

    def get_question_id(self):
        return self.kwargs.get(self.lookup_url_kwarg)

    def get_queryset(self):
        if self.request.method != "GET":
            return Question.objects.filter(author=self.request.user)
        return Question.objects.all()

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise Http404()

        question_id = self.get_question_id()
        question = get_object_or_404(Question, question_id)
        serializer = self.serializer_class(question, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({}, status=404)


class QuestionLikeViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (LoginRequiredMixin,)
    lookup_url_kwarg = "question_id"

    def get_question_id(self):
        return self.kwargs.get(self.lookup_url_kwarg)

    def post(self, request, *args, **kwargs):
        question_id = self.get_question_id()
        like_qs = Like.objects.filter(question_id=question_id)

        if like_qs.exists():
            like_qs.filter(user=request.user).delete()
            return Response({"like_count": like_qs.count()}, status=200)

        Like.objects.create(question_id=question_id, user=request.user)
        return Response({"like_count": like_qs.count()}, status=200)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (LoginRequiredMixin, AllowModifyOnlyAuthorUserMixin,)
    lookup_url_kwarg = "question_id"

    def get_question_id(self):
        return self.kwargs.get(self.lookup_url_kwarg)

    def get_queryset(self):
        question_id = self.get_question_id()
        return self.queryset.filter(question_id=question_id)

    def create(self, request, *args, **kwargs):
        question_id = self.get_question_id()
        serializer = self.get_serializer(data=request.data, question_id=question_id)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)
