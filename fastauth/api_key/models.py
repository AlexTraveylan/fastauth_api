from datetime import datetime, timezone
from enum import Enum

from sqlmodel import Field, SQLModel


class PlanEnum(Enum, str):
    FREE = "free"
    BASIC = "basic"
    PREMIUM = "premium"


class APIKey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    application_name: str = Field(max_length=255)
    plan: PlanEnum
    api_key: str = Field(max_length=255, unique=True)
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
