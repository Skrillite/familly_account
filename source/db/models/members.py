from sqlalchemy import Column, Integer

from .base import BaseModel


class DBMembers(BaseModel):
    __tablename__ = 'members'

    user_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, autoincrement=True)
