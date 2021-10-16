from django.urls import path
from . import views

urlpatterns = [
    path('comments/<str:videoid>/', views.CommentList.as_view()),
    path('comments/<int:id>/Like', views.LikeIt.as_view()),
    path('comments/<int:id>/Dislike', views.DislikeIt.as_view()),

    path('comments/', views.CommentList.as_view()),
    path('replies/', views.ReplyList.as_view()),
    path('comments/<int:id>/', views.CommentDetail.as_view()),
    path('replies/<int:commentid>/', views.ReplyDetail.as_view())
]