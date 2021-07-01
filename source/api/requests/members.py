from pydantic import BaseModel


class ChangingUser(BaseModel):
    user_id: int
    new_user_id: int
