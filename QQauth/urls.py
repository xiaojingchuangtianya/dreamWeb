from django.urls import path
from QQauth import views

urlpatterns=[
    path("login/",views.loginView),
    path("register/",views.registerView),
    path("qqLogin/",views.qqLoginView),
    path("logout/",views.logoutView),
    path("wechat/",views.wechatLink),
]
