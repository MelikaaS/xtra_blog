from django.contrib import admin

from post.models import Category,Post,Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
