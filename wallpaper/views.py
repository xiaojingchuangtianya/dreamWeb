from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse,Http404
from wallpaper.models import ImgType,Picture
from django.db import connection
import MySQLdb
# Create your views here.

def index(request):
    return render(request,"wallpaper/allImgs.html")

#后续转为drf
#返回所有分类
def allType(request):
    allTypes=ImgType.objects.all()
    sendList=[i.typeName for i in allTypes]
    return JsonResponse({"imgTypes":sendList})

#根据类型返回数据，返回该类的数据
def typeImg(request,imgType):

    try:
        typeId=ImgType.objects.get(typeName=imgType).id
    except Exception as e:
        return render(request,"dealPage/404.html")
    with connection.cursor() as cursor:
        cursor.execute("select imgSize,url from wallpaper_picture where imgType_id=%d  limit 0, 24;"%typeId)
        manyTuple =cursor.fetchall()
        manyImg=[[i[0],i[1]] for i in manyTuple]
    response=render(request, "wallpaper/typeImg.html", context={"imgType":imgType,"manyImg":manyImg})
    imgType=imgType.replace(" ","_")
    print(imgType)
    response.set_cookie("{}_page".format(imgType),1,expires=60*60*24)
    return response

def typeNextImg(request):
    imgType=request.GET.get("type",default=None)
    imgType=imgType.replace(" ","_")
    page=request.COOKIES["{}_page".format(imgType)] or None
    #没有该类型直接返回报错
    print(imgType,page)
    try:
        typeId = ImgType.objects.get(typeName=imgType).id
        print(typeId)
    except Exception as e:
        return render(request, "dealPage/404.html")
    if page:
        with connection.cursor() as cursor:
            cursor.execute("select imgSize,url from wallpaper_picture where imgType_id={}  limit {},24;".format(typeId,str(24*int(page))))
            manyTuple = cursor.fetchall()
            if manyTuple == ():
                return JsonResponse(None,safe=False)
            manyImg = [[i[0], i[1]] for i in manyTuple]
        response = JsonResponse(manyImg,safe=False)
        response.set_cookie("{}_page".format(imgType), int(page)+1, expires=60*60*24)
        return response

#根据图片的热度展示
def hottestImg(request):
    return render(request,"wallpaper/hottestImg.html")

#返回随机的25张图片
def randomImg(request):
    with connection.cursor() as cursor:
        cursor.execute("select imgSize,url from wallpaper_picture order by rand() limit 24;")
        manyTuple =cursor.fetchall()
        manyImg=[[i[0],i[1]] for i in manyTuple]
    return render(request,"wallpaper/randomImg.html",context={"manyImg":manyImg})

def nextRandom(request):
    with connection.cursor() as cursor:
        cursor.execute("select imgSize,url from wallpaper_picture order by rand() limit 24;")
        manyTuple =cursor.fetchall()
        manyImg=[[i[0],i[1]] for i in manyTuple]
    return JsonResponse(manyImg,safe=False)

def detail(request,url):
    print(url)
    return render(request,"wallpaper/detail.html",context={"url":url})
