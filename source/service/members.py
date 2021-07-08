from .DI import DI
from api.dto import ChangingUser


async def add_member(dep: DI, db_connection_fabric, data: ChangingUser):
    account_id: int = await dep.db_queries.create_member(db_connection_fabric(), data)
    payment_methods: list[int] = await dep.db_queries.get_payment_method_by_account_id(
        db_connection_fabric(),
        account_id
    )

    await dep.external_queries.add_payment_methods((data.changing_user_id,), payment_methods)


async def delete_member(dep: DI, db_connection_fabric, data: ChangingUser):
    account_id: int = await dep.db_queries.delete_member(db_connection_fabric(), data)
    payment_methods: list[int] = await dep.db_queries.get_payment_method_by_account_id(
        db_connection_fabric(),
        account_id
    )

    await dep.external_queries.delete_payment_methods((data.changing_user_id,), payment_methods)
