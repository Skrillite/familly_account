from aiohttp import ClientSession

from configs import ApplicationConfigs


async def add_payment_method(user_ids: list[int], payment_methods: list[int]):
    async with ClientSession() as session:
        for id in user_ids:
            async with session.post(
                    url=ApplicationConfigs.ext.user_data_service_url,
                    json={
                        'id': id,
                        'payment_methods': payment_methods
                    }
            ) as resp:
                if resp.status != 200:
                    raise Exception


async def delete_payment_method(user_ids: list[int], payment_methods: list[int]):
    async with ClientSession() as session:
        for id in user_ids:
            async with session.delete(
                url=ApplicationConfigs.ext.user_data_service_url,
                json={
                    'id': id,
                    'payment_methods': payment_methods
                }
            ) as resp:
                if resp.status != 200:
                    raise Exception('tmp')