from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import ChatUser, Message

class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatUser
        fields = [ 'id', 'username', 'email', 'contacts', 'messages', 'password']
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender_id', 'receiver_id', 'text', 'is_read', 'sent_at']
