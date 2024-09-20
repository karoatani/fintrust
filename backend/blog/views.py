from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    BlogPost,
    Reaction,
    Comment
    )
from .serializers import (
    BlogPostCreateSerializer,
    BlogPostSerializer,
    BlogPostReactionSerializer,
    BlogCommentSerializer,
    BlogReplySerializer
    )

# Create your views here.



class BlogPostCreateAPIView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateSerializer



class BlogPostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRecentListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


    def get_queryset(self):
        return super().get_queryset().order_by("last_updated")[:5]

class BlogPostReactionAPIView(generics.CreateAPIView):
   queryset = BlogPost.objects.all()
   serializer_class = BlogPostReactionSerializer

   def get_serializer_context(self):
       user = self.request.user
       context = super().get_serializer_context()
       context.update({
           "user" : user
       })
       return context
   

   def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
            
        type_of_reaction = serializer.validated_data.get("type_of_reaction")
        blog_post = serializer.validated_data.get("blog_post")
        reaction = Reaction.objects.filter(blog_post=blog_post,user_that_reacted=self.request.user) 
        if reaction.exists():
            if reaction[0].type_of_reaction == type_of_reaction:
                return Response({
                            "error" : "User already reacted to the given post"
                            }, status=status.HTTP_403_FORBIDDEN)
            else :
                reaction.update(type_of_reaction=type_of_reaction)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
       
   
class BlogPostRemoveReactionAPIView(generics.DestroyAPIView):
   queryset = Reaction.objects.all()
   lookup_field = "blog_id"

   def get_queryset(self):
       user = self.request.user
       blog_post_id = self.kwargs["blog_id"]
       queryset = super().get_queryset().filter(user_that_reacted=user, blog_post=blog_post_id)
       print(queryset)
       return queryset
   
   def destroy(self, request, *args, **kwargs):
        
        queryset = self.get_queryset()
        obj =  get_object_or_404(queryset)
        
        self.check_object_permissions(self.request, obj)
        self.perform_destroy(obj)
        
        return Response(status=status.HTTP_204_NO_CONTENT)





# comment on a particular blog post

class BlogCommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = BlogCommentSerializer


# Work on this later
class BlogReplyAPIView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = BlogReplySerializer
    # lookup_field = "comment_id"

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(self.get_queryset())
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        blog_post = data.pop("blog_post")
        reply = Comment.objects.create(**data)
        print(instance.reply.all())
        # instance.reply.add(reply)
        # instance.save()
        
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
