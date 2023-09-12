from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routers import apis, ws
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from settings import db
import aioredis

main = FastAPI()

main.include_router(ws.router)
main.include_router(apis.router)


async def redis_pool():
    redis = await aioredis.from_url(
        url="redis://127.0.0.1",
        port=6379,
        password="",
        db=0,
        encoding="utf-8",
        decode_responses=True,
    )
    return redis


scheduler = AsyncIOScheduler()


@main.on_event("startup")
async def startup_event():
    """添加在应用程序启动之前运行初始化数据库"""
    register_tortoise(main, db_url=db.db_url, modules={"models": ["app.models.users", "app.models.rooms"]})
    main.state.redis = await redis_pool()


@scheduler.scheduled_job("interval", seconds=60)
def interval_task_test():
    print("interval task is run...")
