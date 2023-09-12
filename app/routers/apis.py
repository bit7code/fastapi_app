from fastapi import APIRouter
from app.internal.conn import manager
from app.models.users import User

router = APIRouter()


@router.post("/api/{user_id}")
async def coin(user_id: str):
    try:
        users = await User.all()
        for user in users:
            print(user.name)
    except Exception as e:
        print(e)
    await manager.send_message(user_id, "nihao")
