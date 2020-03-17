from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from app_account.views import UserAPI
from .views import UserSignUpAPI


urlpatterns = [
    path('login', obtain_auth_token),
    path('sign-up', UserSignUpAPI.as_view()),
    path('info', UserAPI.as_view()),
]
