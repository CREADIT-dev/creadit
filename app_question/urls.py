from django.urls import path
from .views import QuestionViewSet

question_view_set = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'patch': 'update',
    'delete': 'destroy',
})
question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    # TODO : url 추가해주기
    path('', QuestionViewSet.as_view()),
]