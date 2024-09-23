from fastapi import APIRouter, Request

# import stripe
from fastauth.subscriptions.schemas import CheckoutSchemaIn, CheckoutSchemaOut

subscriptions_router = APIRouter(
    tags=["Subscriptions"],
    prefix="/subscriptions",
)


@subscriptions_router.post("/checkout")
def checkout(request: Request, payload: CheckoutSchemaIn) -> CheckoutSchemaOut:
    pass


@subscriptions_router.post("/webhook")
def webhook(request: Request):
    pass
