TORTOISE_ORM = {
    "connections": {"default": "mysql://devops:devops@127.0.0.1:3306/gemapp"},
    "apps": {
        "models": {
            "models": ["models.users", "models.rooms", "aerich.models"],
            "default_connection": "default",
        },
    },
}

db_url = "mysql://devops:devops@127.0.0.1:3306/gemapp"
