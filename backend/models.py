import uuid
from django.db import models
from customuser.models import Account
import datetime

class Approval(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    user = models.ForeignKey('customuser.Account', on_delete=models.CASCADE, blank=True)
    Time = models.DateTimeField(verbose_name="date_created", auto_now_add= True)
    name = models.CharField(max_length=2200, default= "")
    def __str__(self):
        return str(self.name)
    
    
class Decline(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    name = models.CharField(max_length=2200, default= "")
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    Time = models.DateTimeField(verbose_name="date_created", auto_now_add= True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    name = models.CharField(max_length=2200, default= "", )
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    Text = models.TextField(max_length= 400)
    Time = models.DateTimeField(verbose_name="date_created", auto_now_add= True)
    
    def __str__(self):
        return self.name   
    
class Posts(models.Model):
    PostId = models.AutoField(primary_key= True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    Owner = models.ForeignKey(Account,on_delete=models.CASCADE)
    PublishDate = models.DateTimeField(verbose_name="date joined", auto_now_add= True)
    Photo = models.ImageField(verbose_name="post_image", default="default.png", max_length= 3000)
    Title = models.TextField(max_length= 3000)
    Text = models.TextField()
    Tags = models.TextField(max_length= 620)
    Category = models.CharField(max_length= 309)
    ObjectionTo = models.UUIDField(default="00000000-0000-0000-0000-000000000000")
    Approvals = models.ManyToManyField('Approval', blank= True)
    Declines = models.ManyToManyField('Decline', blank= True)
    Comments = models.ManyToManyField('Comment', blank= True)
    Objections = models.ManyToManyField('Posts', blank= True)
    
    def __str__(self):
        return str(self.uuid)

