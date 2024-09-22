from typing import Annotated

from fastapi import Depends
from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from fastauth.common.settings import SETTINGS


def get_engine():
    return create_engine(SETTINGS.DATABASE_URL)


async def create_db_and_tables(engine: Annotated[Engine, Depends(get_engine)]):
    SQLModel.metadata.create_all(engine)


async def get_session(engine: Annotated[Engine, Depends(get_engine)]):
    with Session(engine, autoflush=True) as session:
        yield session
        session.commit()
