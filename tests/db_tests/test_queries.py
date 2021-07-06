import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db import queries
from db.models import DBMembers, DBPayment
from api.requests import BaseRequestData, ChangingUser
from configs import ApplicationConfigs


admins_ids = [1, 2, 3]
members_ids = [
    (1, 11), (1, 12), (1, 13),
    (2, 21), (2, 22), (2, 23),
    (3, 31), (3, 32), (3, 33)
]
payment_methods = [
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


class Test_DBQueries:
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
        session: AsyncSession = pytest.ctx.db.get().make_session()

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

    @pytest.mark.asyncio
    @pytest.mark.parametrize('requesting_user_id, new_user_id', members_ids)
    async def test_new_member(self, requesting_user_id, new_user_id):
        session: AsyncSession = pytest.ctx.db.get().make_session()

        async with session.begin():
            await queries.create_member(
                session,
                ChangingUser.parse_obj({
                    'requesting_user_id': requesting_user_id,
                    'changing_user_id': new_user_id
                })
            )

            nui, = (await session.execute(
                select(DBMembers.user_id).where(DBMembers.user_id == new_user_id)
            )).fetchone()

        assert nui == new_user_id

    @pytest.mark.asyncio
    @pytest.mark.parametrize('requesting_user_id, payment_id', payment_methods)
    async def test_new_payment_method(self, requesting_user_id, payment_id):
        session: AsyncSession = pytest.ctx.db.get().make_session()

        async with session.begin():
            before = (await session.execute(
                select(DBPayment.payment_method_id).where(DBPayment.payment_method_id == payment_id)
            )).fetchone()

            await queries.add_payment_method(session, requesting_user_id, payment_id)

            after, = (await session.execute(
                select(DBPayment.payment_method_id).where(DBPayment.payment_method_id == payment_id)
            )).fetchone()

            assert before is None
            assert after == payment_id
