from transport.configs import SanicConfig
from db.configs import PotgresConfig


class ExternalServices:
    user_data_service_url = 'localhost:0000'


class ApplicationConfigs:
    sanic = SanicConfig
    db = PotgresConfig
    ext = ExternalServices
