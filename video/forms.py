from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "description", "category", "keywords", "video_file", "thumbnail_image"]

