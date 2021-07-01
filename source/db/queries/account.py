from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete

from db.models import DBMembers, DBPayment
from api.requests import UserID, AccountID


async def create_account(session: AsyncSession, data: UserID):
    async with session.begin():
        session.add(
            DBMembers(
                user_id=data.user_id,
            )
        )


async def delete_account(session: AsyncSession, data: AccountID):
    async with session.begin():
        await session.execute(
            delete(DBMembers).where(DBMembers.account_id == data.account_id)
        )
        await session.execute(
            delete(DBPayment).where(DBPayment.account_id == data.account_id)
        )
