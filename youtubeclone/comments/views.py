from django.http.response import Http404
from .models import Comment
from .models import Reply
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Comment Views
class CommentList(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self, videoid):
        try:
            return Comment.objects.filter(videoid=videoid)
        except Comment.DoesNotExist:
            raise Http404

    #get by video id
    def get(self, request, videoid):
        comment = self.get_object(videoid)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    #update
    def put(self, request, videoid):
        comment = self.get_object(videoid)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, videoid):
        comment = self.get_object(videoid)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Reply Views
class ReplyList(APIView):

    def get(self, request):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyDetail(APIView):

    def get_object(self, commentid):
        try:
            return Reply.objects.get(commentid=commentid)
        except Reply.DoesNotExist:
            raise Http404

    #get by id
    def get(self, request, commentid):
        reply = self.get_object(commentid)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)

    #update
    def put(self, request, commentid):
        reply = self.get_object(commentid)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, commentid):
        reply = self.get_object(commentid)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)