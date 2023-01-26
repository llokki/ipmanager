import os
from tortoise import Tortoise
from tortoise.models import Model

async def db_connect():
    mysql_root_password = os.getenv('MYSQL_ROOT_PASSWORD','secret')
    mysql_database = os.getenv('MYSQL_DATABASE','ipmanager')
    mysql_user = os.getenv('MYSQL_USER','admin2')
    mysql_password = os.getenv('MYSQL_PASSWORD','5E1f!bEtTQN')
    mysql_host = os.getenv('MYSQL_HOST','mysql_db')
    await Tortoise.init(
        db_url=f'mysql://{mysql_user}:{mysql_password}@{mysql_host}:3307/{mysql_database}',
        modules={'models': ['app.models_def']}
    )
