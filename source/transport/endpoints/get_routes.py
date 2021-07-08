from . import (
    AccountRoutes,
    Members,
    Payment
)


def get_routes():
    return (
        (AccountRoutes.as_view(), '/account'),
        (Members.as_view(), '/members'),
        (Payment.as_view(), '/payment')
    )
