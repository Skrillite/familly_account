from sanic.views import HTTPMethodView
from sanic import Request, Sanic
from sanic.response import raw

from db import queries
from db.database import DataBase
from api.requests import BaseRequestData
from configs import ApplicationConfigs


class Account(HTTPMethodView):
    def __init__(self):
        self.db: DataBase = Sanic.get_app(ApplicationConfigs.sanic.NAME).ctx.db.get()

    async def post(self, request: Request):
        data: BaseRequestData = BaseRequestData.parse_obj(request.json)

        await queries.create_account(self.db.make_session(), data)
        return raw('', status=201)

    async def delete(self, request: Request):
        data: BaseRequestData = BaseRequestData.parse_obj(request.json)

        await queries.delete_account(self.db.make_session(), data)

        return raw('')
