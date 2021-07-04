from sqlalchemy import Column, Integer, ForeignKey

from .base import BaseModel


class DBPayment(BaseModel):
    __tablename__ = 'payment_methods'

    account_id = Column(Integer, primary_key=True)
    payment_method_id = Column(Integer, primary_key=True)
