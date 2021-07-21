from contextvars import ContextVar

from sanic import Sanic

from configs import ApplicationConfigs
from .endpoints.get_routes import get_routes
from hooks import init_db_posgresql, init_di
from service.DI import DI


def configure_app() -> Sanic:
    app = Sanic(name=ApplicationConfigs.sanic.NAME)
    app.update_config(ApplicationConfigs.sanic)

    for route in get_routes():
        app.add_route(*route)

    app.ctx.db = ContextVar("db_context")
    app.ctx.di: ContextVar[DI] = ContextVar("dep injection")

    init_db_posgresql(app.ctx.db)
    init_di(app.ctx.di)

    return app
