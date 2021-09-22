from django.contrib import admin
from blog.models import BlogType,Blog,Hot

# Register your models here.
admin.site.register(BlogType)
admin.site.register(Blog)
admin.site.register(Hot)
