from .DI import DI

from api.dto import PaymentMethod


async def add_payment_method(dep: DI, db_connection_factory, data: PaymentMethod):
    account_id: int = await dep.db_queries.account_id_by_member(db_connection_factory(), data.requesting_user_id)
    await dep.db_queries.add_payment_method(db_connection_factory(), account_id, data.payment_method_id)

    user_ids: list[int] = await dep.db_queries.members_by_account_id(db_connection_factory(), account_id)

    dep.external_queries.add_payment_methods(user_ids, (data.payment_method_id, ))


async def delete_payment_method(dep: DI, db_connection_factory, data: PaymentMethod):
    account_id: int = await dep.db_queries.account_id_by_member(db_connection_factory(), data.requesting_user_id)
    await dep.db_queries.delete_payment_method(db_connection_factory(), account_id, data.payment_method_id)

    user_ids: list[int] = await dep.db_queries.members_by_account_id(db_connection_factory(), account_id)

    await dep.external_queries.delete_payment_methods(user_ids, data.payment_method_id)
