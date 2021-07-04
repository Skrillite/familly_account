from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete

from db.models import DBMembers, DBPayment
from api.requests import ChangingUser


async def create_member(session: AsyncSession, data: ChangingUser) -> int:
    async with session.begin():
        account_id, = (await session.execute(
            insert(DBMembers).from_select([DBMembers.user_id, DBMembers.account_id],
                                          select(data.changing_user_id, DBMembers.account_id)
                                          .where(DBMembers.user_id == data.requesting_user_id))
                .returning(DBMembers.account_id)
                .execution_options(synchronize_session=False)
        )).fetchone()

        return account_id


async def delete_member(session: AsyncSession, deleting_user_id) -> int:
    async with session.begin():
        account_id, = (await session.execute(
            select(DBMembers.account_id).where(DBMembers.user_id == deleting_user_id)
        )).fetchone()

        await session.execute(
            delete(DBMembers).where(DBMembers.user_id == deleting_user_id)
        )

        return account_id


async def account_id_by_member(session: AsyncSession, user_id: int) -> int:
    async with session.begin():
        account_id, = (await session.execute(
            select(DBMembers.account_id).where(DBMembers.user_id == user_id)
        )).fetchone()

    return account_id


async def members_by_account_id(session: AsyncSession, account_id: int) -> list[int]:
    async with session.begin():
        user_ids = await session.execute(
            select(DBMembers.user_id).where(DBMembers.account_id == account_id)
        )
        user_ids = [i for i, in user_ids.all()]

    return user_ids
