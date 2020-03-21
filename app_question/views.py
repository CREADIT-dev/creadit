from django.http import Http404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from app_question.models.question import Question
from app_question.serializers.question import QuestionSerializer
from mixin import AllowModifyOnlyAuthorUserMixin, LoginRequiredMixin


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (LoginRequiredMixin, AllowModifyOnlyAuthorUserMixin,)

    def get_queryset(self):
        if self.request.method != "GET":
            return Question.objects.filter(author=self.request.user)
        return Question.objects.all()

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise Http404()

        pk = kwargs['pk']
        question = get_object_or_404(Question, pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
