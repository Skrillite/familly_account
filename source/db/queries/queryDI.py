from api.dto import *


async def create_account(db_connection, data: BaseRequestData):
    """Получает id пользователя, сделавшего запрос.
    Если этого пользователя ещё нет в базе, создает запись с этим пользователем
    и новым id аккаунта"""

    raise NotImplemented


async def delete_account(db_connection, data: BaseRequestData):
    """Получает id пользователя, сделавшего запрос.
    Удаляет все записи, связанные с этим аккаунтом из баз members и payment_methods"""

    raise NotImplemented


async def account_id_by_member(db_connection, data: ChangingUser):
    """Получает id запрашивающего и запрашиваемого пользователей
    возвращает id аккаунта запрашиваемого пользователя, либо исключение,
    если у запрашивающего пользователя недостаточно прав"""

    raise NotImplemented


async def members_by_account_id(db_connection, data: ChangingUser):
    raise NotImplemented


async def create_member(db_connection, data: ChangingUser):
    raise NotImplemented


async def delete_member(db_connection, data: ChangingUser):
    raise NotImplemented


async def add_payment_method(db_connection, data: PaymentMethod):
    raise NotImplemented


async def delete_payment_method(db_connection, data: PaymentMethod):
    raise NotImplemented


async def get_payment_method_by_account_id(db_connection, data: ChangingUser):
    raise NotImplemented


class DBQueryDI:
    create_account = create_account
    delete_account = delete_account

    create_member = create_member
    delete_member = delete_member
    account_id_by_member = account_id_by_member
    members_by_account_id = members_by_account_id

    get_payment_method_by_account_id = get_payment_method_by_account_id
    add_payment_method = add_payment_method
    delete_payment_method = delete_payment_method
