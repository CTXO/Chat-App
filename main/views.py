from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators  import api_view, permission_classes
from rest_framework.response import Response
from main.serializers import ChatUserSerializer, MessageSerializer
from .models import ChatUser, Message
from rest_framework import permissions


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def show_all(request):
    users = ChatUser.objects.all()
    serializer = ChatUserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_user(request):
    data = JSONParser().parse(request)
    user = ChatUser.create(data['username'], data['email'], data['password']) # add Generic name later
    serializer = ChatUserSerializer(user)
    return JsonResponse(serializer.data)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def delete_user(request):
    data = JSONParser().parse(request)
    user_id = data['user_id']
    try:
        username = ChatUser.deleteUser(user_id)
        return JsonResponse({'Message':  f'User {username} deleted'})
    except ObjectDoesNotExist:
        return JsonResponse({'Message': 'This id is not valid'})



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def send_message(request):
    data = JSONParser().parse(request)
    sender_id, receiver_id, text = data['sender_id'], data['receiver_id'], data['text']
    sender, receiver = ChatUser.objects.get(pk=sender_id), ChatUser.objects.get(pk=receiver_id)
    message = sender.sendMessage(receiver, text)
    serializer = MessageSerializer(message)
    sender.visualize_chat(receiver)
    return JsonResponse(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def read_chat(request):
    data = JSONParser().parse(request)
    src_user_id, target_user_id = data['src_user_id'], data['target_user_id']
    try:
        src_user, target_user = ChatUser.objects.get(pk=src_user_id), ChatUser.objects.get(pk=target_user_id)
    except ObjectDoesNotExist:
        return JsonResponse({'Message': 'This id is not valid'})

    chat = src_user.list_chat_with(target_user)
    serializer = MessageSerializer(chat, many=True)
    src_user.visualize_chat(target_user)
    return JsonResponse(serializer.data, safe=False)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def add_contact(request):
    data = JSONParser().parse(request)
    src_user_id, target_user_id = data['src_user_id'], data['target_user_id']
    try:
        src_user, target_user = ChatUser.objects.get(pk=src_user_id), ChatUser.objects.get(pk=target_user_id)
    except ObjectDoesNotExist:
        return JsonResponse({'Message': 'This id is not valid'})

    src_user.addContact(target_user)
    serializer = ChatUserSerializer(src_user)
    return JsonResponse(serializer.data)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def delete_contact(request):
    data = JSONParser().parse(request)
    src_user_id, target_user_id = data['src_user_id'], data['target_user_id']
    src_user, target_user = ChatUser.objects.get(pk=src_user_id), ChatUser.objects.get(pk=target_user_id)
    src_user.deleteContact(target_user)
    serializer = ChatUserSerializer(src_user)
    return JsonResponse(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def show_contacts(request):
    data = JSONParser().parse(request)
    src_user_id  = data['src_user_id']
    src_user = ChatUser.objects.get(pk=src_user_id)
    contacts = src_user.contacts.all()
    serializer = ChatUserSerializer(contacts, many=True)
    return JsonResponse(serializer.data, safe=False)
    