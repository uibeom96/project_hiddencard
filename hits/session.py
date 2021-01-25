from django.conf import settings
from main.models import Video


class Hit_Count_Session(object):
    def __init__(self, request):
        self.session = request.session
        hits = self.session.get(settings.HIT_ID)
        if not hits:
            hits = self.session[settings.HIT_ID] = {}

        self.hits = hits
        print(self.hits)

    def add(self, video):
        if str(video.id) not in self.hits:
            video.hit_count += 1
            video.save()            
        self.hits[video.id] = {str(video.author.nick_name): str(video.title) }
        self.saves()


    def saves(self):
        self.session[settings.HIT_ID] = self.hits
        self.session.modified = True


            
