from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('replies/', views.ReplyList.as_view()),
    path('comments/<str:videoid>/', views.CommentDetail.as_view()),
    path('replies/<int:commentid>/', views.ReplyDetail.as_view())
]