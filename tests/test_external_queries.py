import json
from collections import defaultdict
from copy import copy, deepcopy
from random import choice

import pytest
from pytest_aiohttp import aiohttp_client
from aiohttp import web
from logging import getLogger

from configs import ApplicationConfigs
from transport.external_queries import add_payment_method, delete_payment_method

user_id_payment_id = [
    ([1], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3])
]

payment_method_data: dict[int, set[int]] = defaultdict(set)


async def add_payment(request: web.Request):
    methods: dict = await request.json(loads=json.loads)

    payment_method_data[methods['id']] = methods['payment_methods']

    return web.Response(text=await request.text())


async def delete_payment(request: web.Request):
    methods: dict = await request.json(loads=json.loads)

    payment_method_data[methods['id']].difference_update(methods['payment_methods'])

    return web.Response(text=await request.text())


@pytest.fixture
def get_client_session(loop, aiohttp_client):
    app = web.Application()

    app.router.add_post('/payment', add_payment)
    app.router.add_delete('/payment', delete_payment)

    ApplicationConfigs.ext.user_data_service_url = '/payment'

    return loop.run_until_complete(aiohttp_client(app))


@pytest.mark.parametrize('user_ids, payment_ids', user_id_payment_id)
async def test_add_payment_methods(get_client_session, user_ids, payment_ids):
    await add_payment_method(user_ids, payment_ids, get_client_session)

    assert payment_method_data == {user_id: payment_ids for user_id in user_ids}


@pytest.mark.parametrize('user_ids, payment_ids', user_id_payment_id)
async def test_delete_payment_methods(get_client_session, user_ids, payment_ids):
    global payment_method_data
    payment_method_data = {user: set(payment_ids) for user in user_ids}

    deleting_id: int = choice(user_ids)
    before = deepcopy(payment_method_data)

    await delete_payment_method([deleting_id], payment_ids, get_client_session)

    assert before[deleting_id].difference(payment_method_data[deleting_id]) == set(payment_ids)

    for key, value in before.items():
        if key != deleting_id:
            assert payment_method_data[key] == before[key]
