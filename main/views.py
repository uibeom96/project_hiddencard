from django.shortcuts import render
from main.models import Video
from main.models import Comment
from hits.session import Hit_Count_Session
import random

def index(request):
    video_list = Video.objects.filter(is_deleted=False)
    video = random.choice(video_list)
    comments = Comment.objects.filter(video = video)

    a = Hit_Count_Session(request)
    a.add(video)

    return render(request, "main/index.html",   
    {
        "video": video,
        "comments": comments,
    })