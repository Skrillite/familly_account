from api.dto import BaseRequestData


async def create_account(db_connection, data: BaseRequestData):
    """Получает id пользователя, сделавшего запрос.
    Если этого пользователя ещё нет в базе, создает запись с этим пользователем
    и новым id аккаунта"""

    raise NotImplemented


async def delete_account(db_connection, data: BaseRequestData):
    """Получает id пользователя, сделавшего запрос.
    Удаляет все записи, связанные с этим аккаунтом из баз members и payment_methods"""

    raise NotImplemented


class DBQueryDI:
    create_account = create_account
    delete_account = delete_account

