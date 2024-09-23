import logging

from fastauth.database.engine import create_db_and_tables, get_engine

logging.basicConfig(level=logging.INFO)


create_db_and_tables(engine=get_engine())
