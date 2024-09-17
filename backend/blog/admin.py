from django.contrib import admin

from .models import (
    BlogPost,
    Category,
    Tag,
    TableOfContent,
    Comment,
    Reaction

)
# Register your models here.


admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(TableOfContent)
admin.site.register(Comment)
admin.site.register(Reaction)