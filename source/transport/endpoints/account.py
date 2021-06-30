from sanic.views import HTTPMethodView
from sanic.response import json

from db import queries


class Account(HTTPMethodView):
    async def post(self, request):
        pass
