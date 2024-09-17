from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from account.models import Account

class BlogPost(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="author", null=True, blank=True)
    
    user_that_last_updated =  models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user_that_last_updated", null=True, blank=True)
    title = models.CharField(max_length=255)
    
    body = CKEditor5Field('Text', config_name='extends')
    
    
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField("Tag")
    comments = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True, blank=True)
    
    
    is_archive = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)
    views = models.PositiveBigIntegerField(default=0)
    cover_image = models.ImageField(upload_to="cover_images")
    
    table_of_content = models.OneToOneField("TableOfContent", on_delete=models.CASCADE, null=True)
    slug = models.SlugField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

        
    def save(self, **kwargs):
        self.slug = slugify(self.title)
        if (
            update_fields := kwargs.get("update_fields")
        ) is not None and "name" in update_fields:
            kwargs["update_fields"] = {"slug"}.union(update_fields)
        
        super().save(**kwargs)


class Reaction(models.Model):
    blog_post = models.ForeignKey("BlogPost", on_delete=models.CASCADE, null=True, blank=True, related_name="reaction")
    REACTION_CHOICES = [
    ("like", "like"),
    ("dislike", "dislike"),
    ]
    user_that_reacted = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="user_that_like", null=True, blank=True)
    type_of_reaction = models.CharField(max_length=255, choices= REACTION_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = CKEditor5Field('Text', config_name='extends')
    comment = models.ForeignKey("self" , on_delete = models.CASCADE ,null=True, blank=True, related_name="reply")
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    user =  models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    user =  models.ForeignKey(Account, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)



class TableOfContent(models.Model):
    content = CKEditor5Field('Text', config_name='extends')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)



