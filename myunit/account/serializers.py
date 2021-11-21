# serializer(직렬화): 쿼리셋이나 모델 인스턴스같은 복잡한 구조의 데이터를 JSON, XML등 형태로 변환
from os import name
from django.db.models import base, fields
from .models import Profile, CustomUser
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
import base64
import io
from PIL import Image

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # 유효성 검증된 값으로 User 객체 생성
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            phonenum=validated_data['phonenum'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'phonenum']

class ProfileSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Profile
        fields = ['user', 'user_pk', 'nickname', 'photo', 'gender', 'city', 'interest',
                  'skill', 'mycomment', 'portfolio', 'is_open']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
    