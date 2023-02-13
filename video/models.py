import sys
import uuid
import ffmpeg
import subprocess
from django.db import models
from django.conf import settings
from video.categories import CATEGORIES_CHOICES
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="", choices=CATEGORIES_CHOICES)
    keywords = models.CharField(max_length=255, default="")
    video_file = models.FileField(upload_to='videos/', null=True)
    thumbnail_image = models.FileField(upload_to='images/', default="")

    def __str__(self):
        return str(self.name) + ": " + str(self.video_file)


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

