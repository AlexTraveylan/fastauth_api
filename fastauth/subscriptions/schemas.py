from typing import Literal

from pydantic import BaseModel


class CheckoutSchemaOut(BaseModel):
    client_secret: str


class CheckoutSchemaIn(BaseModel):
    subscription_plan: Literal["free", "basic", "premium"]
