from types import FrameType
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.serializers import Serializer
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile, CustomUser
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# 유저 회원가입
class UserCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny,]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

#유저 로그인
# @api_view(['POST'])
# @permission_classes([AllowAny,])
# def LoginAPI(request):
#     email = request.data['email']
#     password = request.data['password']
#     if email is None or password is None:
#         return Response({'error':'이메일과 비밀번호 모두 입력해주세요'},status=HTTP_400_BAD_REQUEST)
#     user = authenticate(email=email,password=password)
#     if not user:
#         return Response({"error":"유효하지 않은 이메일이거나 비밀번호입니다"},status=HTTP_400_BAD_REQUEST)
#     token,created = Token.objects.get_or_create(user=user)
#     return Response({
#         'token':token.key,
#         'user_pk': user.pk,
#         'user_id': user.id,
#         'email':user.email
#     })

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
    lookup_field = "user_pk"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# 프로필 전체목록
@api_view(['GET'])
@permission_classes([AllowAny,])
def AllProfileAPI(request):
    profile = Profile.objects.all()
    serializer = ProfileSerializer(profile,many=True)
    return Response(serializer.data)
