from .account import BaseRequestData


class PaymentMethod(BaseRequestData):
    payment_method_id: int
