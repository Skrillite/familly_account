import aiohttp
from sanic.views import HTTPMethodView
from sanic import Request, Sanic
from sanic.response import raw

from api.requests import PaymentMethod
from db import queries, DataBase
from configs.configs import ApplicationConfigs
from service.DI import DI
from service.payment import add_payment_method, delete_payment_method


class Payment(HTTPMethodView):
    def __init__(self):
        self.db: DataBase = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.db.get()
        self.di: DI = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.di.get()

    async def post(self, request: Request):
        data: PaymentMethod = PaymentMethod.parse_obj(request.json)

        await add_payment_method(self.di, self.db.session_factory, data)

        return raw("", status=201)

    async def delete(self, request: Request):
        data: PaymentMethod = PaymentMethod.parse_obj(request.json)

        await delete_payment_method(self.di, self.db.session_factory, data)

        return raw("", status=200)
