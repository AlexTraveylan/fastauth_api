from datetime import datetime, timezone

from sqlmodel import Field, SQLModel

from fastauth.database.repository import Repository


class UserEmail(SQLModel, table=True):
    __tablename__ = "user_email"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    encoded_email: str
    token: str
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_verified: bool = Field(default=False)


class UserEmailRepository(Repository[UserEmail]):
    __model__ = UserEmail


USER_EMAIL_REPOSITORY = UserEmailRepository()
