import asyncio
from tortoise import Tortoise


async def init():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url="mysql://devops:devops@127.0.0.1:3306/gemapp", modules={"models": ["app.models.users"]}
    )
    # Generate the schema
    # await Tortoise.generate_schemas()


if __name__ == "__main__":
    asyncio.run(init())
