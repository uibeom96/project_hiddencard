from django.db import models
from django.contrib.auth.models import AbstractUser
from config.models import BaseModel

class User(AbstractUser, BaseModel):
    nick_name = models.CharField(max_length=50)


    class Meta:
        db_table = "users"
        verbose_name = "유저들"
        verbose_name_plural = "유저"
        ordering = ("-created", )
    
    def __str__(self):
        return str(self.username)


        
    