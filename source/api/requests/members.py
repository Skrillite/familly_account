from pydantic import BaseModel


class NewUserID(BaseModel):
    user_id: int
    new_user_id: int
