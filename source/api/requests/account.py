from pydantic import BaseModel


class BaseRequestData(BaseModel):
    user_id: int


class AccountID(BaseRequestData):
    account_id: int
