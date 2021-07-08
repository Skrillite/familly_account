from db.queries.queryDI import DBQueryDI
from transport.external_queries.query_interfaces import ExtQueriesDI


class DI:
    external_queries: ExtQueriesDI = ExtQueriesDI
    db_queries: DBQueryDI = DBQueryDI
