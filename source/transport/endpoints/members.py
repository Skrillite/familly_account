from sanic.views import HTTPMethodView
from sanic import Request, Sanic
import aiohttp

from db import queries, DataBase
from api.requests import ChangingUser
from configs import ApplicationConfigs


class Members(HTTPMethodView):
    def __init__(self):
        self.db: DataBase = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.db.get()

    async def post(self, requset: Request):
        data: ChangingUser = ChangingUser.parse_obj(requset.json)

        account_id: int = await queries.create_member(self.db.session_factory(), data.user_id, data.new_user_id)
        payment_methods: tuple = await queries.get_payment_method(self.db.session_factory(), account_id)

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=ApplicationConfigs.ext.user_data_service_url,
                    json=payment_methods
            ) as resp:
                await resp.text()

    async def delete(self, request: Request):
        data: ChangingUser = ChangingUser.parse_obj(request.json)

        account_id: int = await queries.delete_member()