from . import (
    Account,
    Members
)


def get_routes():
    return (
        (Account.as_view(), '/account'),
        (Members.as_view(), '/members')
    )
