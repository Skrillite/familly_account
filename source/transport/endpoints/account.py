from sanic.views import HTTPMethodView
from sanic import Request, Sanic
from sanic.response import raw

from db.database import DataBase
from api.requests import BaseRequestData
from configs import ApplicationConfigs
from service.account import Account
from service.DI import DI


class AccountRoutes(HTTPMethodView):
    def __init__(self):
        self.db: DataBase = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.db.get()
        self.di: DI = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.di.get()

    async def post(self, request: Request):
        data: BaseRequestData = BaseRequestData.parse_obj(request.json)

        await Account.create_account(self.di, self.db.make_session(), data)
        return raw('', status=201)

    async def delete(self, request: Request):
        data: BaseRequestData = BaseRequestData.parse_obj(request.json)

        await Account.delete_account(self.di, self.db.make_session(), data)

        return raw('', status=200)
