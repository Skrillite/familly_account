from os import getenv

from dotenv import load_dotenv
from sanic.config import Config

load_dotenv()


class SanicConfig(Config):
    NAME = "family_account"

    HOST = getenv("HOSTNAME", "localhost")
    PORT = int(getenv("PORT", 8000))
    WORKERS = int(getenv("WORKERS", 1))
    DEBUG = bool(int(getenv("DEBUG", 0)))
