from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool, QueuePool
from contextvars import ContextVar

from configs import ApplicationConfigs
from db.database import DataBase
from db import queries
from db.queries.queryDI import DBQueryDI
from service.DI import DI


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


def init_di(di: ContextVar):
    dbq = DBQueryDI()
    dbq.create_account = queries.create_account
    dbq.delete_account = queries.delete_account

    extq = None

    di.set(DI())
    di.get().db_queries = dbq
    di.get().external_queries = extq
