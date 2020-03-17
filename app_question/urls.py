from django.urls import path
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


urlpatterns = [
    # TODO : url 추가해주기
    path('QnA', question_views),
    path('QnA/<int:question_id>')
]
