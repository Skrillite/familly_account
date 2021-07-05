import aiohttp
from sanic.views import HTTPMethodView
from sanic import Request, Sanic
from sanic.response import raw

from api.requests import PaymentMethod
from db import queries, DataBase
from configs.configs import ApplicationConfigs


class payment(HTTPMethodView):
    def __init__(self):
        self.db: DataBase = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.db.get()

    async def post(self, request: Request):
        data: PaymentMethod = PaymentMethod.parse_obj(request.json)

        account_id: int = await queries.account_id_by_member(self.db.session_factory(), data.requesting_user_id)
        await queries.add_payment_method(self.db.session_factory(), account_id, data.payment_method_id)

        user_ids: list[int] = await queries.members_by_account_id(self.db.session_factory(), account_id)

        async with aiohttp.ClientSession() as session:
            for user in user_ids:
                async with session.post(
                        url=ApplicationConfigs.ext.user_data_service_url,
                        json=data.payment_method_id
                ) as resp:
                    if resp.status != 200:
                        raise Exception # TODO

        return raw('', status=201)

    async def delete(self, request: Request):
        data: PaymentMethod = PaymentMethod.parse_obj(request.json)

        account_id: int = await queries.account_id_by_member(self.db.session_factory(), data.requesting_user_id)
        await queries.delete_payment_method(self.db.session_factory(), account_id, data.payment_method_id)

        user_ids: list[int] = await queries.members_by_account_id(self.db.session_factory(), account_id)

        async with aiohttp.ClientSession() as session:
            for user in user_ids:
                async with session.delete(
                    url=ApplicationConfigs.ext.user_data_service_url,
                    json=data.payment_method_id
                ) as resp:
                    if resp.status != 200:
                        raise Exception # TODO
