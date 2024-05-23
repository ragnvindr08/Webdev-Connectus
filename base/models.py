from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, null=True)
    receiver = models.CharField(max_length=100, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')   