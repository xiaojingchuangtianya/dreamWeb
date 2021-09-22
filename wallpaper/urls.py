from django.urls import path,re_path
from wallpaper import views

#还要作每一个下一页的获取数据内容的接口，方便下翻页加载数据
urlpatterns = [
    path("",views.randomImg),
    path("nextRandom",views.nextRandom),
    re_path("type=(?P<imgType>.+$)",views.typeImg),#最后要作一个re匹配，获取那些类型图片
    re_path(r"typeNextImg",views.typeNextImg),
    path("hottestImg",views.hottestImg),#最热的图片
    path("allType",views.allType),#做一个接口，然后返回随机的一些照片
    re_path(r"detail/(?P<url>\w.*)",views.detail),
]
