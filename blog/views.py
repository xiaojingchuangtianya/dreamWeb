import json
import re
from blog.models import BlogType,Blog,Hot,Comment
from django.shortcuts import render,redirect
from django.http.response import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from blog.myFont import MyForms
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt 



# Create your views here.
def blogHome(request):
    # 这里要做一个热度榜的前10条信息
    tenHotBlog=Blog.objects.get_queryset().order_by("-hot")
    #最近博客访问量 后续再新增
    # 随机的博客推荐（5条左右）
    print(tenHotBlog)
    return  render(request,"blog/blogHome.html",context={"tenHotBlog":tenHotBlog})

#写博客时新增类别时需要修改iframe的内容

@login_required
def writeBlog(request):
    if request.method =="GET":
        myForm=MyForms()
        return render(request,"blog/writeBlog.html",context={"myForm":myForm})
    elif request.method == "POST":
        postData=request.POST
        getBlogType=BlogType.objects.filter(id=postData["type"])
        if not request.user:
            # 非登录用户去登录去
            return redirect("/login")
        # 如果有查寻到已经存在的type，获取，否则新增
        if getBlogType.exists():
            addType=getBlogType[0]
        else:
            addType=BlogType.objects.create(typeName=postData["type"])
        newHot =Hot.objects.create()

        print(postData["title"],newHot,addType,postData["content"],request.user)
        try:
            blog =Blog.objects.create(
                title=postData["title"],
                hot=newHot,
                type=addType,#需要检测是否存在，不存在则新建
                content=postData["content"],
                createTime= now(),
                author =request.user
            )
            return redirect("/blog")
        except Exception as e:
            print(e)
            return HttpResponse("error")


def createType(request):
    typeName = json.loads(request.body.decode("utf-8"))["addType"]
    try:
        BlogType.objects.create(typeName=typeName)
        returnData = {"ResCode": 1, "typeName": typeName}
    except Exception as e:
        returnData={"ResCode":0,"typeName":typeName}
    print(returnData)
    return JsonResponse(returnData)

#在进入博客详情时，同时需要去获取对应的评论内容，返回进行展示
def blogDetail(request,blogId):
      # 保存cookie10个小时
    try:
        blogDet = Blog.objects.get(id=blogId)
        isReadBlog = request.COOKIES.get("isReadBlog{}".format(blogDet.id))
        comments=Comment.objects.filter(blogF=blogDet)
        detResponse = render(request, "blog/blogDetail.html", context={"blog": blogDet,"comments":comments})
        if not isReadBlog:  # 如果没有找到该cookie,给他新增cookie
            detResponse.set_cookie("isReadBlog{}".format(blogDet.id), 1, expires=60*60*5)
            hotDetail =Hot.objects.get(pk=blogDet.hot_id)
            hotDetail.hotRate+=1
            hotDetail.save()
    except Exception as e:
        print(e)
        return render(request, "dealPage/404.html")
    return detResponse

#必须用户已经登录才可以处理
#处理接口，如果新增博客的详情内容，返回1为正确新增，其他为错误
@login_required
@csrf_exempt
def createComent(request):
    dataDict=eval(str(request.body,encoding="utf-8"))
    print(request.user)
    print(dataDict)
    blogf=Blog.objects.get(id=dataDict["blog"])
    commnet=Comment.objects.create(blogF=blogf,userName=str(request.user),writeTime=now(),content=dataDict["Comment"])
    return JsonResponse({"user":str(request.user)})