import uuid
from customuser.models import Account
from backend.models import Posts
import datetime
from django.db import models


class Approval(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,)
    Time = models.DateTimeField(verbose_name="date_created", auto_now_add= True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.uuid    
    
    
class Decline(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    Time = models.DateTimeField(verbose_name="date_created", auto_now_add= True)
    
    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    Text = models.TextField(max_length= 400)
    Time = models.DateTimeField(verbose_name="date_created", auto_now_add= True)
    
    def __str__(self):
        return self.user.username   