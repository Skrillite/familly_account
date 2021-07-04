from pydantic import BaseModel


class BaseRequestData(BaseModel):
    requesting_user_id: int


class AccountID(BaseRequestData):
    account_id: int
