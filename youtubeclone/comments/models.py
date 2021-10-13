from django.db import models

# Create your models here.

class Comment(models.Model):
    videoid = models.TextField(max_length=300)
    comment = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    name = models.TextField(max_length=300)
    likes = models.IntegerField(blank=False, null=False)
    dislikes = models.IntegerField(blank=False, null=False)

class Reply(models.Model):
    commentid = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    name = models.TextField(max_length=300)
    likes = models.IntegerField(blank=False, null=False)
    dislikes = models.IntegerField(blank=False, null=False)
    
