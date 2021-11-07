# serializer(직렬화): 쿼리셋이나 모델 인스턴스같은 복잡한 구조의 데이터를 JSON, XML등 형태로 변환
from .models import Profile, CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # 유효성 검증된 값으로 User 객체 생성
            user = CustomUser.objects.create_user(
                email=validated_data['email'],
                nickname=validated_data['nickname'],
                password=validated_data['password'],
            )
            return user
             
    class Meta:
        model = CustomUser
        fields = ['nickname', 'email', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'photo', 'gender', 'city', 'interest',
                  'skill', 'mycomment', 'portfolio', 'is_open']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
