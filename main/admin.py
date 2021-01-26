from django.contrib import admin
from main.models import Video, Comment

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created")
    list_display_links = ("title", )
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "video", "content", "author",)
    list_display_links = ("content", )


