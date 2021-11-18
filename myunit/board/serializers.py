from .models import Post
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ImageField(use_url=True, max_length=None)
    
    class Meta:
        model = Post
        fields = ['profile', 'title', 'contest',
                  'content', 'poster', 'city', 'interest', 'end_date','is_open', 'recruit']
        read_only_fields = ['profile']

    def create(self, validated_data):
        profile = self.context['request'].user.profile
        validated_data['profile'] = profile
        return super().create(validated_data)
