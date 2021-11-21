from rest_framework import serializers
from chat.models import Message
from account.models import CustomUser, Profile
# 
# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
