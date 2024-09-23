from sqlmodel import Field, SQLModel

from fastauth.database.repository import Repository


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(max_length=255, unique=True)
    password: str = Field(max_length=255)
    api_key_id: int | None = Field(default=None, foreign_key="api_key.id", ondelete="CASCADE")


class UserRepository(Repository[User]):
    __model__ = User


USER_REPOSITORY = UserRepository()
