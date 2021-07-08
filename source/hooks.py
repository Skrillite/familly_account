from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool, QueuePool
from contextvars import ContextVar

from configs import ApplicationConfigs
from db.database import DataBase
from db import queries
from db.queries.queryDI import DBQueryDI
from service.DI import DI
from transport.external_queries.query_interfaces import ExtQueriesDI
from transport import external_queries


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

    dbq.create_member = queries.create_member
    dbq.delete_member = queries.delete_member
    dbq.account_id_by_member = queries.account_id_by_member
    dbq.members_by_account_id = queries.members_by_account_id

    dbq.get_payment_method_by_account_id = queries.get_payment_methods
    dbq.add_payment_method = queries.add_payment_method
    dbq.delete_payment_method = queries.delete_payment_method

    extq = ExtQueriesDI()
    extq.add_payment_methods = external_queries.add_payment_method
    extq.delete_payment_methods = external_queries.delete_payment_method

    di.set(DI())
    di.get().db_queries = dbq
    di.get().external_queries = extq
