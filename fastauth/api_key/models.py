from datetime import datetime, timezone

from sqlmodel import Field, SQLModel

from fastauth.api_key.enums import PlanEnum


class APIKey(SQLModel, table=True):
    __tablename__ = "api_key"

    id: int | None = Field(default=None, primary_key=True)
    application_name: str = Field(max_length=255)
    plan: PlanEnum
    api_key: str = Field(max_length=255, unique=True)
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
