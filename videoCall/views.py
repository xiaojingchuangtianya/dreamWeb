from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def indexVideo(request):
    return render(request,"chat/indexTest.html")

def dealRoom(request,roomName):
    print("进入房间"+roomName)
    return render(request,"chat/roomTest.html",context={"roomName":roomName})

def videoCall(request,roomName,userName):
    return render(request,"chat/video.html",context={"roomName":roomName,"userName":userName})





