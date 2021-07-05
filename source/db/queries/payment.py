from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, delete

from db.models import DBPayment


async def add_payment_method(session: AsyncSession, account_id: int, payment_id: int):
    async with session.begin():
        await session.execute(
            insert(DBPayment).values(
                account_id=account_id,
                payment_method_id=payment_id
            )
        )


async def delete_payment_method(session: AsyncSession, account_id: int, payment_id: int):
    async with session.begin():
        await session.execute(
            delete(DBPayment).where(DBPayment.payment_method_id == payment_id)
        )


async def get_payment_methods(session: AsyncSession, account_id: int) -> set:
    async with session.begin():
        methods = (await session.execute(
            select(DBPayment.payment_method_id).where(DBPayment.account_id == account_id)
        )).all()

        methods = {i for i, in methods}

        return methods
