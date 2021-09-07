from django.db.models.query import QuerySet
from django.shortcuts import render
from .serializers import SecondProfileSerializer, UserSerializer, ProfileSerializer
from .models import Profile, CustomUser, SecondProfile
from rest_framework import generics

# 회원가입


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProfileCreate(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class SecondProfileCreate(generics.CreateAPIView):
    queryset = SecondProfile.objects.all()
    serializer_class = SecondProfileSerializer
