from django.shortcuts import render,redirect
from django.http.response import HttpResponse
import os
from django.conf import settings

def index(request):
    return render(request,"home/index.html")

#注册，后续增加微信账号、qq账号关联直接注册
def register(request):
    pass
#用户可以直接用qq/微信扫码进行登录
def login(request):
    pass
