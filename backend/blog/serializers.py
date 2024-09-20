from rest_framework import serializers
from .models import (
    BlogPost,
    TableOfContent,
    Reaction,
    Comment
    )



class BlogPostTableOfContentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOfContent
        fields = ["content"]

class BlogPostCreateSerializer(serializers.ModelSerializer):
    table_of_content = BlogPostTableOfContentCreateSerializer()
    class Meta:
        model = BlogPost
        fields = ["author", "title", "body", "category", "tags", "comments", "cover_image", "table_of_content"]


    def create(self, validated_data):
        table_of_content = validated_data.pop("table_of_content")
        table_of_content = TableOfContent.objects.create(**table_of_content)
        print(table_of_content)
        instance = super().create(validated_data)
        instance.table_of_content = table_of_content
        instance.save()
        return instance


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "body", "blog_post", "comment"]


class BlogReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "body", "blog_post", "comment"]

class BlogPostSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_dislikes = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ["author", "user_that_last_updated", 
                  "title", "body", "category", "tags", "comments", 
                  "is_archive", "is_draft", "views", 
                  "cover_image", "table_of_content", "slug",
                  "total_likes",
                  "total_dislikes",
                  "date_created",
                  "last_updated",
                  ]

    def get_total_likes(self,obj):
        print(obj)
        return Reaction.objects.filter(blog_post=obj,type_of_reaction="like").count()
    
    
    def get_total_dislikes(self,obj):
        print(Reaction.objects.filter(blog_post=obj))
        return Reaction.objects.filter(blog_post=obj,type_of_reaction="dislike").count()


class BlogPostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ["blog_post","type_of_reaction"]

    def create(self, validated_data):
        user = self.context.get("user")
        instance = super().create(validated_data)
        instance.user_that_reacted = user
        instance.save()
        return instance


