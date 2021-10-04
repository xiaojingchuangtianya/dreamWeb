from django.urls import path,re_path
from blog import views

urlpatterns=[
    path("",views.blogHome),
    path("writeBlog/",views.writeBlog),#处理写博客
    path("createType",views.createType),
    re_path(r"blogDetail/(?P<blogId>\d+)/",views.blogDetail),
    path("createComment",views.createComent),
    re_path(r"getBlog/(?P<id>\d+)",views.getBlog),
]
