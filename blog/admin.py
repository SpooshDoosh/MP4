from django.contrib import admin
from .models import BlogMod, CommentMod

# Register your models here.


admin.site.register(BlogMod)
admin.site.register(CommentMod)