from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self,event):
        print('websocket connected...')

    def websocket_receive(self,event):
        print('websocket received...')

    def websocket_disconnected(self,event):
        print('websoket disconnected...')


from channels.consumer import AsyncConsumer

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print('websocket connected...')

    async def websocket_receive(self,event):
        print('websocket received...')

    async def websocket_disconnected(self,event):
        print('websoket disconnected...')
