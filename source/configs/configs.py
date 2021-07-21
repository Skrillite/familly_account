from transport.configs import SanicConfig
from db.configs import PotgresConfig

from os import getenv


class ExternalServices:
    user_data_service_host = getenv("USER_SERVICE_HOST", "localhost")
    user_data_service_port = getenv("USER_SERVICE_PORT", "9823")
    user_data_service_url = user_data_service_host + ":" + user_data_service_port


class ApplicationConfigs:
    sanic = SanicConfig
    db = PotgresConfig
    ext = ExternalServices
