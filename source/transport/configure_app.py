from contextvars import ContextVar

from sanic import Sanic

from configs import ApplicationConfigs
from .endpoints.get_routes import get_routes
from hooks import init_db_posgresql


def configure_app() -> Sanic:
    app = Sanic(name=ApplicationConfigs.sanic.NAME)
    app.update_config(ApplicationConfigs.sanic)

    for route in get_routes():
        app.add_route(*route)

    app.ctx.db = ContextVar('db_context')
    init_db_posgresql(app.ctx.db)

    return app
