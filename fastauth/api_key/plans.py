from typing import TypedDict

from fastauth.api_key.enums import PlanEnum


class PlanContent(TypedDict):
    max_users: int
    price: int
    nb_domains: int


MAX_USERS_PER_PLAN: dict[PlanEnum, PlanContent] = {
    PlanEnum.FREE: {
        "max_users": 10,
        "price": 0,
        "nb_domains": 1,
    },
    PlanEnum.BASIC: {
        "max_users": 1_000,
        "price": 499,
        "nb_domains": 3,
    },
    PlanEnum.PREMIUM: {
        "max_users": 1_000_000,
        "price": 999,
        "nb_domains": 10,
    },
}
