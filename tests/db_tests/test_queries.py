import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db import queries, DataBase
from db.models import DBMembers, DBPayment
from api.requests import BaseRequestData
from configs import ApplicationConfigs


@pytest.fixture()
async def prepare_db():
    session: AsyncSession = pytest.ctx.db.get().make_session()

    async with session.begin():
        await session.execute('TRUNCATE members, payment_methods RESTART IDENTITY')


class TestQueries:
    @pytest.mark.asyncio
    async def test_connection(self):
        session: AsyncSession = pytest.ctx.db.get().make_session()

        async with session.begin():
            test, = (await session.execute(
                'SELECT current_database()'
            )).fetchone()

        await session.close()

        assert test == ApplicationConfigs.db.test_db_name

    @pytest.mark.asyncio
    async def test_new_account(self):
        session = pytest.ctx.db.get().make_session()
