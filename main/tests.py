from django.test import TestCase
from main.models import ChatUser, Message

class SchemaTest(TestCase):
    user = ChatUser.objects.get(pk=6)
    user2 = ChatUser.objects.get(pk=7)

    user.addContact(user2)

    def test_1(self):
        print("finished")

            
        
