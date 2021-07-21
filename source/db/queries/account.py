from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Query
from sqlalchemy import delete, select

from db.models import DBMembers, DBPayment
from api.requests import BaseRequestData, AccountID


async def create_account(session: AsyncSession, data: BaseRequestData):
    async with session.begin():
        session.add(
            DBMembers(
                user_id=data.requesting_user_id,
            )
        )


async def delete_account(session: AsyncSession, data: BaseRequestData):
    async with session.begin():
        account_id = (
            select(DBMembers.account_id)
            .where(DBMembers.user_id == data.requesting_user_id)
            .scalar_subquery()
        )

        await session.execute(
            delete(DBPayment)
            .where(DBPayment.account_id == DBMembers.account_id)
            .where(DBMembers.user_id == data.requesting_user_id)
            .execution_options(synchronize_session=False)
        )

        await session.execute(
            delete(DBMembers)
            .where(DBMembers.account_id == account_id)
            .execution_options(synchronize_session=False)
        )
