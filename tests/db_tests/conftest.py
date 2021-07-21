from contextvars import ContextVar

import pytest

from hooks import init_db_posgresql


@pytest.fixture(scope="module", autouse=True)
def init_db(init):
    pytest.ctx.db = ContextVar("database")
    init_db_posgresql(pytest.ctx.db, test_db=True)

    yield
