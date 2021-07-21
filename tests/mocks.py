from asyncio import sleep
import json

from aiohttp import web


class UserServiceMocks:
    def __init__(self, app: web.Application):
        self.user_payment_data: dict[int, set[int]] = dict()

        self.bind(app)

    def bind(self, app: web.Application):
        app.router.add_post("/payment", self.add_payment_method)
        app.router.add_delete("/payment", self.delete_payment_method)
        app.router.add_get("/payment/{user_id}/", self.show_payment_method)

    async def add_payment_method(self, request: web.Request):
        methods: dict = await request.json(loads=json.loads)

        self.user_payment_data[methods["id"]] = methods["payment_methods"]

        return web.Response(text=await request.text())

    async def delete_payment_method(self, request: web.Request):
        methods: dict = await request.json(loads=json.loads)

        self.user_payment_data[methods["id"]].difference_update(
            methods["payment_methods"]
        )

        return web.Response(text=await request.text())

    async def show_payment_method(self, request: web.Request):
        user_id = request.match_info["user_id"]
        await sleep(0.01)

        web.json_response(list(self.user_payment_data[user_id]))
