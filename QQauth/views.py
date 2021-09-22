from QQauth.loginTool import QQAuth
from dreamWeb import settings
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login,logout

#注册接口，下面的qqLogin可以调用接口新增
def registerView(request):
    if request.method=="GET":
        return render(request,"register.html")
    else:
        redirectUrl = request.GET.get("redirectUrl", "/")
        name = request.POST.get("name", None)
        email =request.POST.get("email",None)
        password = request.POST.get("password", None)
        passwordAgain= request.POST.get("passwordAgain", None)
        if password != None and password==passwordAgain:
            #处理用户是否存在的问题
            ifUser=User.objects.filter(username=name)
            if ifUser:
                return render(request,"register.html",context={"error":"账号已经存在，请使用其他账号!"})
            else:
                LoginUser=User.objects.create_user(username=name,email=email,password=passwordAgain)
                login(request,LoginUser)
                return redirect(redirectUrl)
        else:
            return render(request,"register.html",context={"error":"两次密码需要一致且不为空!"})


#登陆界面可以选择跳转到具体的页面，这个页面记住redirectUrl，然后如果到微信或者qq登陆时也会传过去，最终登陆成功自动跳转
def loginView(request):
    
    if request.method =="GET":
        redirectUrl = request.GET.get("redirectUrl", "/")
        print(request.GET.get("redirectUrl",None))#一个跳转的url
        return render(request,"login.html",context={"redirect":redirectUrl})
    elif request.method =="POST":
        redirectUrl = request.GET.get("redirectUrl", "/")
        name=request.POST.get("name",None)
        password=request.POST.get("password",None)
        if name and password:
            authUser=authenticate(username=name,password=password)
            if authUser:
                login(request,user=authUser)
                return redirect(redirectUrl)
            else:
                return render(request,"login.html",context={"error":"账号或密码不正确！"})

#用户可以直接用qq/微信扫码进行登录
def qqLoginView(request):
    redirectUrl=request.GET.get("redirectUrl", "/")
    #get请求直接打开qq登录界面,访问这个界面先去向qq发起一个请求，返回一个二维码，通过二维码的验证进行登录
    if request.method == "GET":
        authObj=QQAuth(settings.QQ_CLIENT_ID,settings.QQ_CLIENT_SECRET,redirectUrl)
        loginUrl=authObj.createURL()
        print(loginUrl)
        return render(request,"qqlogin.html")

    return HttpResponse("测试成功")


def logoutView(request):
    logout(request)
    return redirect("/")