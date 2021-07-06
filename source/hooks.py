from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool, QueuePool
from contextvars import ContextVar

from configs import ApplicationConfigs
from db.database import DataBase


def init_db_posgresql(database_context: ContextVar, test_db=False):
    url = ApplicationConfigs.db.url
    pool_class = QueuePool

    if test_db:
        url = ApplicationConfigs.db.test_db_url
        pool_class = NullPool

    engine = create_async_engine(
        url,
        pool_pre_ping=True,
        poolclass=pool_class
    )

    database = DataBase(engine)

    database_context.set(database)
