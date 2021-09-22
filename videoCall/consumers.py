import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print(self.scope)
        print(self.scope["url_route"])
        # self.room_name = self.scope['url_route']['kwargs']['roomName']
        self.room_name="test"
        self.room_group_name = 'chat_%s' % self.room_name


        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    #从websocket接受到信息，进行处理
    async def receive(self, text_data):
        # Send message to room group
        #将信息隔天到特定处理函数，发送到群组
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',#处理的函数名字
                'sendData': text_data
            }
        )

    # Receive message from room group
    #处理上面的数据
    async def chat_message(self, event):
        print(event)
        await self.send(text_data=json.dumps(event["sendData"]))
