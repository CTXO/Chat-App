from django.test import TestCase
from main.models import ChatUser, Message
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class SchemaTest(TestCase):
    
    user = User.objects.create_user('Cartaxo', 'email@email.br', 'mypass', first_name='Romero', last_name='Cartaxo')

    def test_1(self):
        print((self.user.username, self.user.password))

            
        
