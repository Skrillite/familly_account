from sqlalchemy.ext.asyncio import AsyncSession

from db.models import DBMembers


async def new_account(session: AsyncSession, user_id):
    session.add(
        DBMembers(
            user_id=user_id
        )
    )
