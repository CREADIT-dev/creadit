from django.urls import path

from app_question.views.answer import (
    AnswerViewSet,
    AnswerLikeViewSet
)
from app_question.views.question import (
    QuestionViewSet,
    QuestionLikeViewSet
)

questions = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

question = QuestionViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy',
})

question_like = QuestionLikeViewSet.as_view({'post': 'post'})

answers = AnswerViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

answer_like = AnswerLikeViewSet.as_view({'post': 'post'})

urlpatterns = [
    path('', questions, name="qna"),
    path('<int:question_id>', question, name="qna_detail"),
    path('<int:question_id>/like', question_like, name="qna_like"),
    path('<int:question_id>/answer', answers, name="answer"),
    path('<int:question_id>/answer/<int:answer_id>/like', answer_like, name="answer")
]
