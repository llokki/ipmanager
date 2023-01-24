import os
from tortoise import Tortoise
from tortoise.models import Model

async def db_connect():
    key = 'MYSQL_ROOT_PASSWORD'
    mysql_root_password = os.getenv(key,"secret")
    key = 'MYSQL_DATABASE'
    mysql_database = os.getenv(key,"ipmanager")
    key = 'MYSQL_USER'
    mysql_user = os.getenv(key,"admin2")
    key = 'MYSQL_PASSWORD'
    mysql_password = os.getenv(key,"5E1f!bEtTQN")
    key = 'MYSQL_HOST'
    mysql_host = os.getenv(key,"mysql_db")
 
    await Tortoise.init(
        db_url=f'mysql://{mysql_user}:{mysql_password}@127.0.0.1:3306/{mysql_database}',
        modules={'models': ['app.models_def']}
    )
