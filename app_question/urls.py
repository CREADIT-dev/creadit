from django.urls import path

from app_question.views import AnswerViewSet
from app_question.views import QuestionLikeViewSet
from .views import QuestionViewSet


question_views = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy',
})

question_like = QuestionLikeViewSet.as_view({'post': 'post'})

answer = AnswerViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('', question_views, name="qna"),
    path('<int:question_id>', question_detail, name="qna_detail"),
    path('<int:question_id>/like', question_like, name="qna_like"),
    path('<int:question_id>/answer', answer, name="answer")
]
