from . import (
    Account
)


def get_routes():
    return (
        (Account.as_view(), '/account'),
    )
