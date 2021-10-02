
from .serializers import PostSerializer
from account.serializers import ProfileSerializer
from .models import Post
from rest_framework import generics, response

# Create your views here.
class PostCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer