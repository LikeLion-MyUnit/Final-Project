from .models import Post
from rest_framework import serializers
from account.serializers import ProfileSerializer
from account.models import Profile


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['profile', 'title', 'contest',
                  'content', 'poster', 'city', 'interest', 'end_date','is_open', 'recruit']
        read_only_fields = ['profile']

    def create(self, validated_data):
        profile = self.context['request'].user.profile
        validated_data['profile'] = profile
        return super().create(validated_data)
