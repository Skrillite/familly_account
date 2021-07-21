import pytest

from transport.configure_app import configure_app


@pytest.fixture(scope="session", autouse=True)
def run_server():
    app = configure_app()
    app.run()
