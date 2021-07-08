from contextvars import ContextVar

from .DI import DI
from api.dto import BaseRequestData


class Account:
    @staticmethod
    async def create_account(dep: DI, db_connection, data: BaseRequestData):
        await dep.db_queries.create_account(db_connection, data)

    @staticmethod
    async def delete_account(dep: DI, db_connection, data: BaseRequestData):
        await dep.db_queries.delete_account(db_connection, data)

