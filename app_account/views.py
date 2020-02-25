from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from rest_framework.response import Response

from app_account.models import User


class UserSignUpView(CreateView):
    pass
