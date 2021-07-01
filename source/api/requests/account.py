from pydantic import BaseModel


class UserID(BaseModel):
    user_id: int

class AccountID(BaseModel):
    account_id: int
