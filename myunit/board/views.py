from django.shortcuts import render, redirect, get_object_or_404
from .serializers import PostSerializer
from account.serializers import ProfileSerializer
from account.models import Profile
from .models import Post
from rest_framework import generics, response, serializers
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


# 게시글 작성
class PostCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 게시글 수정, 삭제
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 게시글 좋아요 기능
@login_required
def post_like_toggle(request, pk):
    post = generics.get_object_or_404(Post, id=pk)
    user = request.user
    profile = Profile.objects.get(user=user)
    check_like_post = profile.like_posts.filter(id=pk)

    if check_like_post.exists():
        profile.like_posts.remove(post)
        post.like_count -= 1
        post.save()
    else:
        profile.like_posts.add(post)
        post.like_count += 1
        post.save()

    return

# 게시글 전체목록
@api_view(['GET'])
@permission_classes([AllowAny,])
def AllPostAPI(request):
    post = Post.objects.all()
    serializer = PostSerializer(post,many=True)
    return Response(serializer.data)
