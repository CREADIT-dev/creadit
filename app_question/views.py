from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from app_question.models.question import Question
from app_question.serializers.question import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = (TokenAuthentication,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }

    def get_queryset(self):
        if self.request.method != "GET":
            return Question.objects.filter(author=self.request.user)
        return Question.objects.all()

    # def get_permissions(self):
    #     # TODO : 권한관리 추가하기, (글 작성자와 어드민만 수정, 삭제 가능)
    #     if self.action in ['',]:
    #         return True
    #     return False
