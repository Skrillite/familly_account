from sqlalchemy.ext.asyncio import create_async_engine
from contextvars import ContextVar

from configs import ApplicationConfigs
from db.database import DataBase


def init_db_posgresql(database_context: ContextVar):
    engine = create_async_engine(
        ApplicationConfigs.db.url,
        pool_pre_ping=True,
    )

    database = DataBase(engine)

    database_context.set(database)
