from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import VideoForm
from .models import Video
from django.views.decorators.csrf import ensure_csrf_cookie
import random


@ensure_csrf_cookie
@login_required
def upload_video(request):
    """Upload video page"""
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        new_user = form.save(commit=False)
        new_user.user = request.user

        req = request.FILES
        temp_file = req.get("video_file")
        temp_file_path = temp_file.temporary_file_path()
        name = request.POST.get("name")

        if form.is_valid():
            form.save_m2m()
            form.save()

    else:
        form = VideoForm()
    return render(request, 'upload_display_video.html', {'form': form})


def handle_uploaded_file(f):
    """Handle file upload for upload view"""
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def show_video(request, id_hash):
    """For the play video page."""
    video = Video.objects.get(pk=id_hash)
    video_file = video.video_file
    name = video.name
    thumb_nail = video.thumbnail_image
    print(f"THUMBNAIL URL = {thumb_nail}")
    print(name)
    context = {"filename": video_file, "MEDIA_URL": "/media", "name": name, "thumbnail": thumb_nail}
    return render(request, "test.html", context)


def show_random_video(request):
    """View to show random video"""
    videos = Video.objects.all()
    id_hash = random.choice(videos).id
    return redirect('/show_video/' + str(id_hash))


def test_view(request):
    """Test the last video in the database"""
    video = Video.objects.last()
    video_file = video.video_file
    name = video.name
    thumb_nail = video.thumbnail_image
    print(f"THUMBNAIL URL = {thumb_nail}")
    print(name)
    context = {"filename": video_file, "MEDIA_URL": "/media", "name": name, "thumbnail": thumb_nail}
    return render(request, "test.html", context)


def home_page(request):
    """Just a test home page"""
    video_list = Video.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(video_list, 12)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    context = {"videos": videos, "MEDIA_URL": "/media"}
    return render(request, "home.html", context)
