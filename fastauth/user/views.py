from fastapi import APIRouter

user_router = APIRouter(tags=["Users"])


@user_router.post("/register")
def register():
    pass


@user_router.post("/token")
def login():
    pass


@user_router.get("/users/me")
def user_me():
    pass
