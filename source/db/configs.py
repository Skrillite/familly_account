import os

from dotenv import load_dotenv

load_dotenv()


class PotgresConfig():
    name = os.getenv('POSTGRES_DB', 'family_account')
    test_db_name = os.getenv('TEST_POSTGRES_DB', 'test_family_account')
    user = os.getenv('POSTGRES_USER', '')
    password = os.getenv('POSTGRES_PASSWORD', '')
    host = os.getenv('POSTGRES_HOST', 'localhost')
    port = os.getenv('POSTRES_PORT', '5432')
    url = rf'postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}'

    alembic_url = rf'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'
    test_db_url = rf'postgresql+asyncpg://{user}:{password}@{host}:{port}/{test_db_name}'
