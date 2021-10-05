from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser

class ChatUser(AbstractUser):
    contacts = models.ManyToManyField('self', symmetrical=False)
    messages = models.ManyToManyField('self', through='Message', through_fields=('sender', 'receiver'))

    #TODO: Make email unique;
    @classmethod
    def create(cls, username, email, password):
        user = cls(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def sendMessage(self, user, text):
        m = Message.objects.create(sender=self, receiver=user, text=text)
        m.save()
        return m
        #print("message sent successfully to " + user.username)

    def addContact(self, user):
        self.contacts.add(user)
        self.save()
        #print(user.username + " was added to your contact list")

    def deleteUser(id):
        user = ChatUser.objects.get(pk=id)
        username = user.username
        user.delete()
        return username
    
    def deleteContact(self, user):
        self.contacts.remove(user)
        self.save()

    def list_chat_with(self, user):
        messagesWithUser = Q(Q(sender=self) & Q(receiver=user)) | Q(Q(sender=user) & Q(receiver=self))
        chat = Message.objects.all().filter(messagesWithUser)
        return chat

    def visualize_chat(self, user):
        chat = self.list_chat_with(user)
        for message in chat:
            message.is_read=True
            message.save()
    
        


class Message(models.Model):
    sender = models.ForeignKey(ChatUser, on_delete=models.SET_NULL, related_name='sender', null=True)
    receiver = models.ForeignKey(ChatUser, on_delete=models.SET_NULL, related_name='receiver', null=True)
    text = models.TextField()
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, sender, receiver, text):
        message = cls(sender=sender, receiver=receiver, text=text)
        return message

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('sent_at',)

    
