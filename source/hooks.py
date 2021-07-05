from sqlalchemy.ext.asyncio import create_async_engine
from contextvars import ContextVar

from configs import ApplicationConfigs
from db.database import DataBase


def init_db_posgresql(database_context: ContextVar, test_db=False):
    url = ApplicationConfigs.db.url
    if test_db:
        url = ApplicationConfigs.db.test_db_url

    engine = create_async_engine(
        url,
        pool_pre_ping=True,
    )

    database = DataBase(engine)

    database_context.set(database)
