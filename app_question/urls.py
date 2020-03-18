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
    path('', question_views, name="qna"),
    path('<int:pk>', question_detail, name="qna_detail")
]
