from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile, CustomUser
from rest_framework import generics


# 유저 회원가입
class UserCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# 유저 업데이트. 삭제
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# 유저 프로필 생성
class ProfileCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# 유저 프로필 업데이트, 삭제
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

