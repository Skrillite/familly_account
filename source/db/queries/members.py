from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql.expression import Insert

from db.models import DBMembers, DBPayment


async def new_member(session: AsyncSession, admin_id, new_user_id) -> int:
    async with session.begin():
        accout_id, = (await session.execute(
            Insert.from_select([DBMembers.user_id, DBMembers.account_id],
                               select(new_user_id, DBMembers.account_id)
                               .where(DBMembers.user_id == admin_id))
                .returning(DBMembers.account_id)
                .execution_options(synchronize_session=False)
        )).fetchone()

        return accout_id


async def get_payment_method(session: AsyncSession, account_id: int) -> tuple:
    async with session.begin():
        methods = (await session.execute(
            select(DBPayment.payment_method_id).where(DBPayment.account_id == account_id)
        )).all()

        return methods
