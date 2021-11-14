from rest_framework import serializers
from chat.models import Message
from account.models import CustomUser
# 
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """For Serializing User"""
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['nickname', 'password']

# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='nickname', queryset=CustomUser.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='nickname', queryset=CustomUser.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']