from django.urls import re_path,path

from videoCall.consumers import ChatConsumer

#asgi程序去处理消费序列
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<roomName>\S.*)/$',ChatConsumer.as_asgi()),
]
