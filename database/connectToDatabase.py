from tortoise import Tortoise
from tortoise.models import Model
async def db_connect():
    await Tortoise.init(
        db_url='mysql://admin2:5E1f!bEtTQN@127.0.0.1:3306/ipmanager',
        modules={'models': ['app.models_def']}
    )
