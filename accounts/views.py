from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from video.models import Video


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def profile_page(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        videos = Video.objects.filter(user=request.user)

        context = {
            "username": username,
            "email": email,
            "videos": videos,
                   }
        return render(request, "registration/profile.html", context=context)
    else:
        return HttpResponseRedirect("/accounts/login/")

