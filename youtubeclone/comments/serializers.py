from rest_framework import serializers
from .models import Comment
from .models import Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'videoid', 'comment', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'commentid', 'reply']
