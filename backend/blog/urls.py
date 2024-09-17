from django.urls import path
from .views import (
    BlogPostCreateAPIView,
    BlogPostRetrieveAPIView,
    BlogPostListAPIView,
    BlogPostReactionAPIView,
    BlogPostRemoveReactionAPIView
    
)

urlpatterns = [
    path("post/create/", BlogPostCreateAPIView.as_view(), name="blog-create"),
    path("post/list/", BlogPostListAPIView.as_view(), name="blog-list"),
    path("post/list/<int:pk>/", BlogPostRetrieveAPIView.as_view(), name="blog-retrieve"),
    path("post/reaction/", BlogPostReactionAPIView.as_view(), name="blog-reaction"),
    path("post/reaction/remove/<int:blog_id>/", BlogPostRemoveReactionAPIView.as_view(), name="blog-reaction-remove")
]