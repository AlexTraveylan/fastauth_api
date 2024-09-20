from sqlmodel import Field, SqlModel


class User(SqlModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(max_length=255, unique=True)
    password: str = Field(max_length=255)
    api_key_id: int | None = Field(default=None, foreign_key="api_key.id", ondelete="CASCADE")
