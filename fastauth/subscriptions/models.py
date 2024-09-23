from datetime import datetime, timezone

from sqlmodel import Field, SQLModel

from fastauth.database.repository import Repository
from fastauth.subscriptions.enums import PaymentStatus


class Subscription(SQLModel, table=True):
    __tablename__ = "subscriptions"

    id: int | None = Field(default=None, primary_key=True)
    amount: int
    stripe_transaction_id: str
    api_key_id: int = Field(foreign_key="api_key.id")
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: PaymentStatus


class SubscriptionRepository(Repository[Subscription]):
    __model__ = Subscription


SUBSCRIPTION_REPOSITORY = SubscriptionRepository()
