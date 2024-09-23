from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from fastauth.common.settings import SETTINGS


def get_engine():
    return create_engine(SETTINGS.DATABASE_URL)


def create_db_and_tables(engine: Engine):
    SQLModel.metadata.create_all(engine)


def get_session(engine: Engine):
    with Session(engine) as session:
        yield session
        session.commit()
