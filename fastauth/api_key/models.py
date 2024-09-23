from datetime import datetime, timezone

from sqlmodel import Field, SQLModel

from fastauth.api_key.enums import PlanEnum
from fastauth.database.repository import Repository


class APIKey(SQLModel, table=True):
    __tablename__ = "api_key"

    id: int | None = Field(default=None, primary_key=True)
    application_name: str = Field(max_length=255)
    plan: PlanEnum
    api_key: str = Field(max_length=255, unique=True)
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))


class APIKeyRepository(Repository[APIKey]):
    __model__ = APIKey


API_KEY_REPOSITORY = APIKeyRepository()


class Domain(SQLModel, table=True):
    __tablename__ = "domains"

    id: int | None = Field(default=None, primary_key=True)
    url: str = Field(max_length=255, unique=True)
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    api_key_id: int = Field(foreign_key="api_key.id", ondelete="CASCADE")


class DomainRepository(Repository[Domain]):
    __model__ = Domain


DOMAIN_REPOSITORY = DomainRepository()
