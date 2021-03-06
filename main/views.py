from django.shortcuts import render, redirect, get_object_or_404
from main.models import Video
from user.models import User
from main.models import Comment
from hits.session import Hit_Count_Session
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
import random, json

@login_required
def index(request):
    page = request.GET.get("page", 1)

    video_list = Video.objects.filter(is_deleted=False)
    video = random.choice(video_list)
    comments = Comment.objects.filter(video = video)

    page_count = Paginator(comments, 5)
    page_object = page_count.get_page(page)

    a = Hit_Count_Session(request)
    a.add(video)

    return render(request, "main/index.html",   
    {
        "video": video,
        "comments": page_object,
    })


def ajax_like(request):
    if request.is_ajax():
        video_id = request.GET.get("video_id")
        video = Video.objects.get(id=video_id)

        if not request.user.is_authenticated:
            message = "로그인을 해주세요"
            context = {"like_count": video.like.count(), "message": message}
            return HttpResponse(json.dumps(context), content_type="application/json")

        if request.user in video.like.all():
            message = "좋아요를 취소했어요!"
            video.like.remove(request.user)
        else: 
            message = "좋아요를 눌렀습니다! "
            video.like.add(request.user)

        context = {'like_count' : video.like.count(), "message": message, "test": "1"}
        return HttpResponse(json.dumps(context), content_type="application/json")

def ajax_dis_like(request):
    if request.is_ajax():
        video_id = request.GET.get("video_id")
        video = Video.objects.get(id=video_id)

        if not request.user.is_authenticated:
            message = "로그인을 해주세요"
            context = {"dis_like_count": video.dis_like.count(), "message": message}
            return HttpResponse(json.dumps(context), content_type="application/json")

        if request.user in video.dis_like.all():
            message = "싫어요를 취소했어요!"
            video.dis_like.remove(request.user)
        else: 
            message = "싫어요를 눌렀습니다! "
            video.dis_like.add(request.user)

        context = {'dis_like_count' : video.dis_like.count(), "message": message}
        return HttpResponse(json.dumps(context), content_type="application/json") 
        
def ajax_follower(request):
    if request.is_ajax():
        author_id = request.GET.get("author_id")
        author = User.objects.get(id=author_id)

        if not request.user.is_authenticated:
            message = "로그인을 해주세요"
            context = {"follow_count": author.follower.all().count(), "message": message}
            return HttpResponse(json.dumps(context), content_type="application/json")

        if author == request.user:
            message = ""
            context = {"follow_count": author.follower.all().count(), "message": message}
            return HttpResponse(json.dumps(context), content_type="application/json")

        if request.user in author.follower.all():
            message = "팔로우를 취소 했어요!"
            author.follower.remove(request.user)
            print(author.follower.all())
        else:
            message = "팔로우를 했어요!"
            author.follower.add(request.user)
            print(author.follower.all())
        context = {"follow_count":   author.follower.all().count(), "message": message}
        return HttpResponse(json.dumps(context), content_type="application/json") 


def ajax_comment(request, pk):
    if request.is_ajax():
        video = get_object_or_404(Video, id=pk)

        if len(request.POST.get("content")) == 0:
            message = "최소 1글자 이상 작성해주세요"
            context = {"message": message}
            return HttpResponse(json.dumps(context), content_type="application/json") 

        Comment.objects.create(
            author=request.user,
            video=video,
            content=request.POST.get("content"))

        context = {
            "comment": request.POST.get("content"),
            "author": str(request.user),
            }

        return HttpResponse(json.dumps(context), content_type="application/json") 