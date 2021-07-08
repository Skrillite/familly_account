from contextvars import ContextVar

from .DI import DI
from api.dto import BaseRequestData


async def create_account(dep: DI, db_connection_factory, data: BaseRequestData):
    await dep.db_queries.create_account(db_connection_factory(), data)


async def delete_account(dep: DI, db_connection_factory, data: BaseRequestData):
    await dep.db_queries.delete_account(db_connection_factory(), data)
