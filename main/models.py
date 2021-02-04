from django.db import models
from config.models import BaseModel
from django.conf import settings


class Video(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.FileField(upload_to="video/%Y-%m-%d")
    title = models.CharField(max_length=15) 
    hit_count = models.IntegerField(default=0)
    content = models.TextField(blank=True)
    hash_tag = models.CharField(max_length=10, blank=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")
    dis_like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="dis_likes")

    class Meta:
        db_table = "video"
        ordering = ("-created", )
        verbose_name = "비디오들"
        verbose_name_plural = "비디오"

    def __str__(self):
        return self.title
        

class Comment(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)

    class Meta:
        db_table = "comment"
        ordering = ("-created", )
        verbose_name = "댓글들"
        verbose_name_plural = "댓글"

    def __str__(self):
        return self.content






