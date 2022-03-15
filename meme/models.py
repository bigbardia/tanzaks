from django.db import models
from karbar.models import Karbar

class MemeManager(models.Manager):

    def newest_memes(self):
        return self.model.objects.all().order_by("-timestamp")

    def most_liked(self):
        return self.model.objects.all().order_by("-likes")

class Meme(models.Model):
    
    image = models.ImageField(upload_to = "memes")
    title = models.CharField(max_length=50)

    user = models.ForeignKey(Karbar , on_delete=models.CASCADE , related_name="user")
    likes = models.ManyToManyField(Karbar)

    timestamp = models.DateTimeField(auto_now_add=True)

    objects = MemeManager()

    def __str__(self):
        return self.user.username + " "  + self.title
