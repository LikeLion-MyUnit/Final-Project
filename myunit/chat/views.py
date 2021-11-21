from django.http.response import JsonResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from chat.models import Message 
from chat.serializers import MessageSerializer # Our Serializer Classes
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
import json


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
@csrf_exempt
def Message_Post(request):
    data = json.loads(request.body)
    serializer = MessageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def Message_Get(request,sender,receiver):
    messages = Message.objects.filter(Q(sender=sender,receiver=receiver) | Q(sender=receiver,receiver=sender))
    serializer = MessageSerializer(messages, many=True, context={'request': request})

    for message in messages:
        message.is_read = True
        message.save()
    return JsonResponse(serializer.data, safe=False)
