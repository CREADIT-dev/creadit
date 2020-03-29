from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from app_question.models import Answer
from app_question.models.like import AnswerLike
from app_question.serializers.answer import AnswerSerializer
from mixin import AllowModifyOnlyAuthorUserMixin
from mixin import LoginRequiredMixin


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


class AnswerLikeViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (LoginRequiredMixin,)
    lookup_url_kwarg = "answer_id"

    def get_answer_id(self):
        return self.kwargs.get(self.lookup_url_kwarg)

    def post(self, request, *args, **kwargs):
        answer_id = self.get_answer_id()
        like_qs = AnswerLike.objects.filter(answer_id=answer_id)

        if like_qs.exists():
            like_qs.filter(user=request.user).delete()
            return Response({"like_count": like_qs.count()}, status=200)

        AnswerLike.objects.create(answer_id=answer_id, user=request.user)
        return Response({"like_count": like_qs.count()}, status=200)