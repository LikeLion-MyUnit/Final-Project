from .models import Category, Post
from rest_framework import serializers
from account.serializers import ProfileSerializer
from account.models import Profile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['profile', 'title', 'contest', 'category', 'poster', 'city', 'interest', 'end_date']

    def create(self,validated_data):
        profile = self.context['request'].user.profile
        validated_data['profile'] = profile
        return super().create(validated_data)