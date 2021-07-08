from sanic.views import HTTPMethodView
from sanic import Request, Sanic

import service
from service.DI import DI
from db import DataBase
from api.requests import ChangingUser
from configs import ApplicationConfigs


class Members(HTTPMethodView):
    def __init__(self):
        self.db: DataBase = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.db.get()
        self.di: DI = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.di.get()

    async def post(self, request: Request):
        data: ChangingUser = ChangingUser.parse_obj(request.json)

        await service.add_member(self.di, self.db.session_factory, data)

    async def delete(self, request: Request):
        data: ChangingUser = ChangingUser.parse_obj(request.json)

        await service.delete_member(self.di, self.db.session_factory, data)
