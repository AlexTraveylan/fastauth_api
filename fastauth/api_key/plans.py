from fastauth.api_key.enums import PlanEnum

MAX_USERS_PER_PLAN: dict[PlanEnum, int] = {
    PlanEnum.FREE: 10,
    PlanEnum.BASIC: 1_000,
    PlanEnum.PREMIUM: 10_000_000,
}
