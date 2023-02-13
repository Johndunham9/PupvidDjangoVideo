import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pupvid.settings")
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
django.setup()
print("PATH")
print(sys.path)
from video.models import *

the_vid = Video.objects.last()
print("Creating 100 video copies")

for count in range(100):
    vid_obj_copy = Video()
    vid_obj_copy.name = "test " + str((count + 1))
    vid_obj_copy.description = "duplicate test video"
    vid_obj_copy.category = the_vid.category
    vid_obj_copy.keywords = the_vid.keywords
    vid_obj_copy.user = the_vid.user
    vid_obj_copy.video_file = the_vid.video_file
    vid_obj_copy.thumbnail_image = the_vid.thumbnail_image
    vid_obj_copy.save()
    print(f"video copy {(count + 1)}")

print("Completed test videos duplication")

