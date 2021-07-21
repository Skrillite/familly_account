from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker


class DataBase:
    connection: AsyncEngine
    session_factory: sessionmaker

    def __init__(self, engine: AsyncEngine):
        self.engine = engine
        self.session_factory = sessionmaker(
            bind=self.engine, expire_on_commit=True, class_=AsyncSession
        )

    def make_session(self) -> AsyncSession:
        return self.session_factory()
