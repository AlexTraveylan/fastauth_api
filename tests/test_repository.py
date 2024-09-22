from typing import Optional

import pytest
from sqlmodel import Field, Session, SQLModel, select

from fastauth.common.exception import NotFoundError
from fastauth.database.repository import Repository


class TestModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int


class TestModel2(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    other_field: str


class RepositoryTest(Repository[TestModel]):
    __model__ = TestModel


REPOSITORY_TEST = RepositoryTest()


class RepositoryTest2(Repository[TestModel2]):
    __model__ = TestModel2


REPOSITORY_TEST2 = RepositoryTest2()


def test_create(session: Session):
    item = TestModel(name="test", age=1)
    item = REPOSITORY_TEST.create(session, item)

    items_in_db = session.exec(select(TestModel)).all()

    assert len(items_in_db) == 1

    assert item.name == "test"


def test_get_or_raise(session: Session):
    item = TestModel(name="test", age=1)
    item = REPOSITORY_TEST.create(session, item)

    item = REPOSITORY_TEST.get_or_raise(session, name="test")

    assert item.name == "test"


def test_get_or_raise_not_found(session: Session):
    with pytest.raises(NotFoundError):
        REPOSITORY_TEST.get_or_raise(session, name="test")


def test_get_all(session: Session):
    item_1 = TestModel(name="test_1", age=1)
    REPOSITORY_TEST.create(session, item_1)
    item_2 = TestModel(name="test_2", age=2)
    REPOSITORY_TEST.create(session, item_2)
    item_3 = TestModel(name="test_3", age=3)
    REPOSITORY_TEST.create(session, item_3)

    items = REPOSITORY_TEST.get_all(session)

    assert len(items) == 3


def test_delete(session: Session):
    item = TestModel(name="test", age=1)
    item = REPOSITORY_TEST.create(session, item)

    assert REPOSITORY_TEST.delete(session, item.id) is True


def test_delete_not_found(session: Session):
    item = TestModel(name="test", age=1)
    item = REPOSITORY_TEST.create(session, item)

    assert REPOSITORY_TEST.delete(session, item.id + 1) is False


def test_update(session: Session):
    item = TestModel(name="test", age=1)
    item = REPOSITORY_TEST.create(session, item)
    item = REPOSITORY_TEST.update(session, item.id, name="test2")
    assert item.name == "test2"


def test_get_or_none(session: Session):
    item = TestModel(name="test", age=1)
    item = REPOSITORY_TEST.create(session, item)

    assert REPOSITORY_TEST.get_or_none(session, name="test") == item


def test_get_or_none_not_found(session: Session):
    assert REPOSITORY_TEST.get_or_none(session, name="test") is None


def test_get_or_raise_with_different_model(
    session: Session,
):
    item = TestModel(name="test", age=1)
    REPOSITORY_TEST.create(session, item)

    item_2 = TestModel2(other_field="test")
    REPOSITORY_TEST2.create(session, item_2)

    item = REPOSITORY_TEST.get_or_raise(session, name="test")
    item_2 = REPOSITORY_TEST2.get_or_raise(session, other_field="test")

    assert item.name == "test"
    assert item_2.other_field == "test"
