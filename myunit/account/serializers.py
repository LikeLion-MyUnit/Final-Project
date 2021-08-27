# serializer(직렬화): 쿼리셋이나 모델 인스턴스같은 복잡한 구조의 데이터를 JSON, XML등 형태로 변환
from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # 유효성 검증된 값으로 User 객체 생성
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            password = validated_data['password'],
            city = validated_data['city'],
            status = validated_data['status'],
            department = validated_data['department'],
            skill = validated_data['skill'],
            interest = validated_data['interest']
        )
        return user
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password','city', 'status', 'department', 'skill', 'interest']