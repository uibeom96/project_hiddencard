from django.db import models
from django.utils import timezone
from datetime import datetime

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False, blank=True)

    class Meta:
        abstract = True

    def delete(self, using=None, Keep_parents=False):
        self.is_deleted = True
        self.deleted = timezone.now()
        self.save()


    