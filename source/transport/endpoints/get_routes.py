from . import (
    AccountRoutes,
    Members
)


def get_routes():
    return (
        (AccountRoutes.as_view(), '/account'),
        (Members.as_view(), '/members')
    )
