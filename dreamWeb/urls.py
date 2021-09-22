"""dreamWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from dreamWeb import views
from wallpaper import urls as wallpaper
from blog import urls as blog
from django.conf.urls.static import static
from dreamWeb.settings import MEDIA_ROOT, MEDIA_URL
from videoCall import urls as videoCall
from QQauth import urls as QQauth

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("wallpaper/",include(wallpaper)),
    path("blog/",include(blog)),
    path("video/",include(videoCall)),
    path("auth/",include(QQauth)),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),#ckeditor的上传路径
]+ static(MEDIA_URL, document_root=MEDIA_ROOT) #没有这一句无法显示上传的图片
