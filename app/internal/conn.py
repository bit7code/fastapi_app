from typing import Dict

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        # 存放激活的ws连接对象
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, user_id: str, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections[user_id] = ws

    def disconnect(self, user_id):
        # 关闭时 移除ws对象
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def send_message(self, user_id: str, message: str):
        # 发送个人消息
        ws = self.active_connections.get(user_id, None)
        if not ws:
            print("用户连接已不存在")
            return
        await ws.send_text(message)

    async def broadcast(self, message: str):
        # 广播消息
        for _, connection in self.active_connections.items():
            await connection.send_text(message)

    def get_connect(self, user_id):
        if user_id not in self.active_connections:
            return None
        return self.active_connections[user_id]


manager = ConnectionManager()
