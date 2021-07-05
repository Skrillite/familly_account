from types import SimpleNamespace

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def init():
    load_dotenv()

    pytest.ctx = SimpleNamespace()
