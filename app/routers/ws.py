import asyncio
from app.internal.conn import manager
from fastapi import WebSocket, WebSocketDisconnect, APIRouter

router = APIRouter()


@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(user_id, websocket)

    await manager.send_message(user_id, f"用户{user_id}进入聊天室")

    redis_client = websocket.app.state.redis
    result = await redis_client.get("aaa")
    print(result)

    try:
        while True:
            # await websocket.receive_text()
            await manager.send_message(user_id, "sshshshsh")
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        manager.disconnect(user_id)
        await manager.broadcast(f"用户-{user_id}-离开")
