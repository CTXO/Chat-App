from django.db import models
from django.contrib.auth.models import AbstractUser

class ChatUser(AbstractUser):
    contacts = models.ManyToManyField('self', symmetrical=False)
    messages = models.ManyToManyField('self', through='Message')

    @classmethod
    def create(cls, username, email, password):
        user = cls(username=username, email=email, password=password)
        return user

    def sendMessage(self, user, text):
        message = Message.create(self, user, text)
        message.save()
        print("message sent successfully to " + user.username)

    def addContact(self, user):
        self.contacts.add(user)
        self.save()
        print(user.username + " was added to your contact list")

    def deleteUser(self):
        self.delete()
    
    def deleteContact(self, user):
        self.contacts.remove(user)
        self.save()


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

    
