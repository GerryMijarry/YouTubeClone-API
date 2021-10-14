from rest_framework import serializers
from .models import Comment
from .models import Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['videoid', 'comment', 'datetime', 'name', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['commentid', 'reply', 'datetime', 'name', 'likes', 'dislikes']
