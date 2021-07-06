import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db import queries, DataBase
from db.models import DBMembers, DBPayment
from api.requests import BaseRequestData
from configs import ApplicationConfigs


admins_ids = [1, 2, 3]
members_ids = [
    (1, 11), (1, 12), (1, 13),
    (2, 21), (2, 22), (2, 23),
    (3, 31), (3, 32), (3, 33)
]


@pytest.fixture()
async def prepare_db():
    session: AsyncSession = pytest.ctx.db.get().make_session()

    yield
    async with session.begin():
        await session.execute('TRUNCATE members, payment_methods RESTART IDENTITY')


class TestQueries:
    @pytest.mark.asyncio
    async def test_connection(self, prepare_db):
        session: AsyncSession = pytest.ctx.db.get().make_session()

        async with session.begin():
            test, = (await session.execute(
                'SELECT current_database()'
            )).fetchone()

        assert test == ApplicationConfigs.db.test_db_name

    @pytest.mark.asyncio
    @pytest.mark.parametrize('id', admins_ids)
    async def test_new_account(self, id: int):
        session = pytest.ctx.db.get().make_session()

        async with session.begin():
            before = (await session.execute(
                select(DBMembers.user_id)
            )).all()

            await queries.create_account(
                session,
                BaseRequestData.parse_obj({
                    'requesting_user_id': id
                }))

            after = (await session.execute(
                select(DBMembers.user_id)
            )).all()

        assert set(before + [(id, )]) == set(after)


# TODO переписать транзакции в ручки
