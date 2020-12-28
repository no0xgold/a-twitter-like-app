from django.conf import settings
import random
from django.db import models


User = settings.AUTH_USER_MODEL
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """
    so each user can have a lot of tweets
    and now on_delete is used when you delete a user, all of his detail including tweets,profile and pictures will be deleted
    but if you want to keep that tweets you can set nul true 
    """ 
    content=models.TextField(blank=True,null=True)
    imagefield=models.FileField(upload_to='images/',blank=True,null=True)

    class Meta:
        ordering = ['-id']
    
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }