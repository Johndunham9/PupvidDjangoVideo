from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    model = Video
    readonly_fields = ('id',)


admin.site.register(Video, VideoAdmin)

