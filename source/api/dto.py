class BaseRequestData:
    requesting_user_id: int


class AccountID(BaseRequestData):
    account_id: int


class ChangingUser(BaseRequestData):
    changing_user_id: int


class PaymentMethod(BaseRequestData):
    payment_method_id: int


class DTODI:
    BaseRequestData = BaseRequestData
    AccountID = AccountID
    ChangingUser = ChangingUser
    PaymentMethod = PaymentMethod
