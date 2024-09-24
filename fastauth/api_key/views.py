from fastapi import APIRouter

api_key_router = APIRouter(
    tags=["API Key"],
    prefix="/api-key",
)


@api_key_router.post()
def create_api_key():
    pass


@api_key_router.post("/{api_key_id}/domains")
def add_domain_to_api_key():
    pass
