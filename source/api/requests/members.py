from .account import BaseRequestData


class ChangingUser(BaseRequestData):
    changing_user_id: int
