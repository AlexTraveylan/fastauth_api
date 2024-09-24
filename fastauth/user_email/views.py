from fastapi import APIRouter

user_email_router = APIRouter(
    tags=["User Email"],
    prefix="/user-emails",
)


@user_email_router.post()
def create_user_email():
    pass


@user_email_router.get("/verify/{token}")
def verify_user_email(token: str):
    pass
