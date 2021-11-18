from rest_framework import serializers
from chat.models import Message
from account.models import CustomUser, Profile
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
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
