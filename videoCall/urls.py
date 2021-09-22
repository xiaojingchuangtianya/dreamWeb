from django.urls import path,re_path
from videoCall import views

urlpatterns=[
    path("",views.indexVideo),
    re_path("room/(?P<roomName>\S.*)/(?P<userName>\S.*)",views.videoCall)
]
