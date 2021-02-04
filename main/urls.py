from django.urls import path, include
from main import views


app_name = "main"

urlpatterns = [
    path("ajax_likes/", views.ajax_like, name="ajax_like"),
    path("ajax_dis_likes/", views.ajax_dis_like, name="ajax_dis_like"),
    path("ajax_follower/", views.ajax_follower, name="ajax_follower"),
    path("ajax_comment/<int:pk>/", views.ajax_comment, name="ajax_comment"),
    path("", views.index, name="index"),
]