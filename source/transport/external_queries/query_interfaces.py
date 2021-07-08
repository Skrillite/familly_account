async def add_payment_methods(user_ids: list[int], payment_methods: list[int]):
    raise NotImplemented


async def delete_payment_methods(user_ids: list[int], payment_methods: list[int]):
    raise NotImplemented


class ExtQueriesDI:
    add_payment_methods = add_payment_methods
    delete_payment_methods = delete_payment_methods
