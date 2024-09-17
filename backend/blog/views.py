from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    BlogPost,
    Reaction
    )
from .serializers import (
    BlogPostCreateSerializer,
    BlogPostSerializer,
    BlogPostReactionSerializer
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
