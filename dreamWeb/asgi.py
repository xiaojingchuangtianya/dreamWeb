import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from videoCall.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dreamWeb.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),#这个指向支持http连接
    #websocket的连接处理以及认证
    "websocket":AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
