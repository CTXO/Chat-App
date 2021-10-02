from django.test import TestCase
from main.models import ChatUser, Message
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class SchemaTest(TestCase):
    romero = ChatUser.objects.get(pk=6)
    ashlyn = ChatUser.objects.get(pk=7)
    john = ChatUser.objects.get(pk=8)
    crenea = ChatUser.objects.get(pk=11)

    #romero.sendMessage(ashlyn, "Hey Ashlyn")
    #romero.sendMessage(ashlyn,  "How you doing?")
    #ashlyn.sendMessage(romero, "Im fine, wby?")
    #romero.sendMessage(ashlyn,  "I can't sleep until i finish this")

    #romero.sendMessage(john, "hey john, its romero")
    #john.sendMessage(crenea, "hey crenea, this is john")
    #john.sendMessage(romero,"hey romero")
    #ashlyn.sendMessage(john, "Hey man, where are u????")
    #crenea.sendMessage(romero, "How do I make John stop texting me???")
    #crenea.sendMessage(romero, "I have more things to do")
    print(john.list_chat_with(romero).values('sender', 'text','is_read'))
    john.visualize_chat(romero)
    print(john.list_chat_with(romero).values('sender', 'text','is_read'))
    def test_1(self):
        pass    
        
