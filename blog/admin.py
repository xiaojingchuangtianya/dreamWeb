from django.contrib import admin
from blog.models import BlogType,Blog, Comment,Hot

# Register your models here.
admin.site.register(BlogType)
admin.site.register(Blog)
admin.site.register(Hot)
admin.site.register(Comment)