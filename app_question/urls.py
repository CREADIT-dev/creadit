from django.urls import path

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

answer
urlpatterns = [
    path('', question_views, name="qna"),
    path('<int:pk>', question_detail, name="qna_detail"),
    path('<int:pk>/like', question_like, name="qna_like")
]
