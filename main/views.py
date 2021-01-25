from django.shortcuts import render
from main.models import Video
from main.models import Comment
import random

def index(request):
    video_list = Video.objects.filter(is_deleted=False)
    video = random.choice(video_list)
    comments = Comment.objects.filter(video = video)
    return render(request, "main/index.html",   
    {
        "video": video,
        "comments": comments,
    })