from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Comment(models.Model):
    
    sno = models.AutoField(primary_key=True)
    url = models.CharField(default=None,blank=True,max_length=3000)
    cmnt = models.TextField(default=None)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)
    
