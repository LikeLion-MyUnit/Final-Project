from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chat.models import Message 
from chat.serializers import MessageSerializer # Our Serializer Classes
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
import json

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def message_list(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        messages = Message.objects.filter(sender=data["sender"], receiver=data["receiver"])
        serializer = MessageSerializer(messages, many=True, context={'request': request})

        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

